from fastapi import FastAPI, Request, status, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from routes.data_processing_routes import data_processing_router
from routes.label_routes import label_router
from routes.scanner_routes import scanner_router
from routes.pallet_crud_routes import pallet_crud_router
from routes.pallet_modifications_routes import combine_pallets_router
# from routes.pallet_lists_routes import pa
from routes.pallet_item_crud_routes import pallet_item_crud_router
from routes.pallet_item_list_routes import pallet_item_list_router

from presentation_layer.product_controllers.product_controllers import get_all_products, get_product_by_id, get_finished_product_by_id, get_all_finished_products

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

# PRODUCT ROUTES
@app.get("/products")
async def find_all_products_function():
    return_item = await get_all_products()
    return return_item
@app.get("/products/{id}")
async def find_product_by_id_function(id):
    return_item = await get_product_by_id(id)
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
app.include_router(combine_pallets_router)
# app.include_router(pallet_list)
app.include_router(pallet_item_crud_router)
app.include_router(pallet_item_list_router)
