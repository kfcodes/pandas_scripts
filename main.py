from fastapi import FastAPI, Request, status, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from routes.data_processing_routes import data_processing_router
from routes.label_routes import label_router
from routes.scanner_routes import scanner_router
from routes.pallet_crud_routes import pallet_crud_router
from routes.pallet_item_crud_routes import pallet_item_crud_router

from presentation_layer.product_controllers.product_controllers import get_all_products, get_product_by_id, get_finished_product_by_id, get_all_finished_products
from presentation_layer.assembly_controllers.assembly_information_controllers import get_all_brands, get_products_from_brand, get_assembly_information

from presentation_layer.production_schedule_controllers.production_schedule_controller import get_all_production, get_current_production, get_production_records_by_id

from presentation_layer.finished_product_controllers.finished_product_crud_controllers import create_finished_product, get_finished_product, update_finished_product, delete_finished_product_by_id

from presentation_layer.production_overview_controllers.production_overview_controllers import get_production_overview, update_production_overview, get_product_overview

import os
from dotenv import load_dotenv
load_dotenv(".env")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# WEBSOCKET MANAGER
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)
manager = ConnectionManager();

@app.get("/update_production_overview", response_class=HTMLResponse)
async def get_current_production_overview_function():
    html_data = update_production_overview();
    return HTMLResponse(content=html_data, status_code=200)
@app.get("/get_production_overview", response_class=HTMLResponse)
async def get_production_overview_function():
    html_data = get_production_overview();
    return HTMLResponse(content=html_data, status_code=200)
@app.websocket("/current_production")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try: 
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You have updated the Current product to: {data}", websocket)
            await manager.broadcast(f"{data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client has left the chat")
@app.get("/get_product_overview/{product_id}", response_class=HTMLResponse)
async def get_product_overview_function(product_id):
    html_data = get_product_overview(product_id);
    return HTMLResponse(content=html_data, status_code=200)


@app.get("/product/{id}")
async def get_product_function(id: str):
    response = await get_product(id);
    return response

# PALLET ROUTES
@app.post("/pallet")
async def create_new_pallet_function():
    pallet_id = await create_pallet()
    return pallet_id
@app.get("/pallet/{id}")
async def find_pallet_function(id):
    pallet = await get_pallet(id)
    return pallet
@app.put("/pallet/{id}")
async def update_pallet_function(id: int, request: Request):
    data =  await request.json();
    pallet = await update_pallet(id, data)
    return pallet
@app.delete("/pallet/{id}")
async def delete_pallet_function(id):
    pallet = await delete_pallet(id)
    return pallet
# @app.post("/combine_pallets")
# async def combine_function(pallet_list:list,height:int):
#     response = await combine_pallets_import(pallet_list, height)
#     return response
# PALLET ITEM ROUTES
@app.post("/pallet_item/{id}")
async def create_pallet_item_function(id):
    item = await create_pallet_item_with_id(id)
    return item
@app.get("/pallet_items/{id}")
async def find_pallet_items_function(id):
    items = await get_items_on_pallet(id)
    return items
@app.put("/pallet_item/{id}")
async def update_pallet_item_function(id):
    item = await update_pallet_item(id)
    return item
@app.delete("/pallet_item/{id}")
async def delete_pallet_item_function(id):
    item = await delete_pallet_item(id)
    return item
@app.get("/new_pallet_items")
async def find_new_pallet_items_function():
    pallet_items = await get_new_pallet_items();
    return pallet_items
@app.get("/all_pallet_items")
async def find_all_pallet_items_function():
    pallet_items = await get_all_pallet_items();
    return pallet_items

# PALLET LIST ROUTES
@app.get("/pallets/{id}")
async def pallet_group_function(id):
    pallets = await get_pallet_group(id)
    return pallets;
@app.get("/all_pallets")
async def find_all_pallets_function():
    pallets = await get_all_pallets()
    return pallets;
@app.get("/pallet_details/{id}")
async def find_pallet_details_function(id):
    pallet_details = await get_pallet_details(id)
    return pallet_details;
@app.get("/possible_pallets")
async def find_possible_pallets_function():
    pallets = await get_possible_pallets()
    return pallets;
@app.get("/new_pallets")
async def find_recent_pallets_function():
    pallets = await get_recent_pallets()
    return pallets
@app.get("/pallet_data")
async def find_pallet_data_function():
    pallet_data = await get_pallet_data()
    return pallet_data;
@app.get("/latest_pallet_data")
async def find_latest_pallet_data_function():
    pallet_data = await get_latest_pallet_data()
    return pallet_data;
@app.get("/picklist")
async def find_picklist_function():
    pallet_data = await get_picklist()
    return pallet_data;
@app.get("/data")
async def find_data_function():
    data = await get_data()
    return data;
@app.post("/data/{id}")
async def find_data_for_id_function(id):
    data = await get_data_for_id(id)
    return data;

# FINISHED PRODUCTS ROUTES
@app.post("/finished_product")
async def create_new_finished_product_function(request: Request):
    data =  await request.json();
    response = await create_finished_product(data)
    return response;
@app.get("/finished_product/{id}")
async def find_finished_product_function(id):
    finished_product = await get_finished_product_by_id(id)
    return finished_product
@app.put("/finished_product/{id}")
async def update_finished_product_function(id, request: Request):
    data =  await request.json();
    finished_product = await update_finished_product(id, data)
    return finished_product
@app.delete("/finished_product/{id}")
async def delete_finished_product_function(id):
    finished_product = await delete_finished_product_by_id(id)
    return finished_product
@app.get("/finished_products/{id}")
async def finished_product_group_function(group_id):
    finished_products = await get_finished_product_by_id(group_id)
    return finished_products
@app.get("/all_finished_products")
async def find_all_Finished_Products_function():
    return_item = get_all_finished_products()
    return return_item
@app.get("/finished_products/{id}")
async def find_finished_product_by_id_function(id):
    return_item = await get_finished_product_by_id(id)
    return return_item

# PRODUCT ROUTES
@app.get("/products")
async def find_all_products_function():
    return_item = await get_all_products()
    return return_item
@app.get("/products/{id}")
async def find_product_by_id_function(id):
    return_item = await get_product_by_id(id)
    return return_item

# BRAND ROUTES
@app.get("/brands/")
async def find_all_brands_function():
    return_item = await get_all_brands()
    return return_item
@app.get("/brandproducts/{id}")
async def brand_products_function(id):
    return_item = await get_products_from_brand(id)
    return return_item
@app.get("/assembly/{id}")
async def assembly_info_function(id):
    # return_item = await get_assembly_information(id)
    return_item = "Got Data"
    return return_item

# PRODUCTION ROUTES
@app.get("/production")
async def find_current_production_function():
    return_item = await get_current_production()
    return return_item;
@app.get("/production/{id}")
async def find_all_production_by_id_function(id):
    return_item = await get_all_production(id)
    return return_item;
@app.get("/production_record/{id}")
async def find_production_record_by_id_function():
    return_item = await get_production_records_by_id(id)
    return return_item;

@app.get("/packing_lists")
async def find_all_packing_lists():
    get_all_packing_lists()
    return {"message": "found packing Lists"}

app.include_router(data_processing_router)
app.include_router(label_router)
app.include_router(scanner_router)
app.include_router(pallet_crud_router)
app.include_router(pallet_item_crud_router)
