from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from presentation_layer.product_controllers.product_controllers import get_product_by_id

# CRUD operation api_route_layer
from api_route_layer.pallet_crud_routes import pallet_crud_router
from api_route_layer.pallet_item_crud_routes import pallet_item_crud_router
from api_route_layer.pallet_group_crud_routes import pallet_group_crud_router

# OTHER ROUTES
from api_route_layer.pallet_lists_routes import pallet_list_router
from api_route_layer.pallet_item_list_routes import pallet_item_list_router
from api_route_layer.label_routes import label_router
from api_route_layer.scanner_routes import scanner_router

# TESTING
# from api_route_layer.assembly_info_routes import assembly_router
from api_route_layer.finished_product_crud_routes import finished_product_router
# from api_route_layer.finished_product_list_routes import finished_product_list_router
# from api_route_layer.production_overview import app as production_overview
# from api_route_layer.production_schedule_routes import schedule_router

# NOT WORKING ROUTES
from api_route_layer.pallet_modifications_routes import combine_pallets_router
from api_route_layer.data_processing_routes import data_processing_router

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

@app.get("/product/{id}")
async def get_product_function(id: str):
    response = await get_product_by_id(id);
    return response;

# @app.get("/packing_lists")
# async def find_all_packing_lists():
#     get_all_packing_lists()
#     return {"message": "found packing Lists"}

# INCLUDE CRUD ROUTES
app.include_router(pallet_crud_router)
app.include_router(pallet_item_crud_router)
app.include_router(pallet_group_crud_router)

# INCLUDE OTHER ROUTES
app.include_router(pallet_list_router)
app.include_router(pallet_item_list_router)
app.include_router(label_router)
app.include_router(scanner_router)
# app.include_router(assembly_router)
app.include_router(finished_product_router)
# app.include_router(finished_product_list_router)
# app.include_router(production_overview)
# app.include_router(schedule_router)
app.include_router(data_processing_router)

# ROUTES NOT WORKING
app.include_router(combine_pallets_router)
