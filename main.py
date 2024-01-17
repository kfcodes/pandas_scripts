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
from routes.assembly_info_routes import assembly_router
from routes.finished_product_crud_routes import finished_product_router
from routes.finished_product_list_routes import finished_product_list_router
# from routes.production_overview import app as fin

from presentation_layer.production_schedule_controllers.production_schedule_controller import get_all_production, get_current_production, get_production_records_by_id

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

# @app.get("/product/{id}")
# async def get_product_function(id: str):
#     response = await get_product(id);
#     return response


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

# @app.get("/packing_lists")
# async def find_all_packing_lists():
#     get_all_packing_lists()
#     return {"message": "found packing Lists"}

app.include_router(data_processing_router)
app.include_router(label_router)
app.include_router(scanner_router)
app.include_router(pallet_crud_router)
app.include_router(combine_pallets_router)
# app.include_router(pallet_list)
app.include_router(pallet_item_crud_router)
app.include_router(pallet_item_list_router)
app.include_router(assembly_router)
app.include_router(finished_product_router)
app.include_router(finished_product_list_router)
