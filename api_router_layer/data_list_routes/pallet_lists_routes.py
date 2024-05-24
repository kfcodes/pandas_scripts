from fastapi import APIRouter
from data_presentation_layer.data_controller_layer.pallet_controllers.pallet_group_controllers import get_pallet_group, get_all_pallets, get_pallet_details, get_possible_pallets, get_recent_pallets, get_pallet_data, get_latest_pallet_data, get_data_for_id, get_data, get_picklist, get_pallet_summary

pallet_list_router = APIRouter();

# PALLET LIST ROUTES
@pallet_list_router.get("/pallets/{id}")
async def pallet_group_function(id):
    pallets = await get_pallet_group(id)
    return pallets;

@pallet_list_router.get("/all_pallets")
async def find_all_pallets_function():
    pallets = await get_all_pallets()
    return pallets;

@pallet_list_router.get("/pallet_details/{id}")
async def find_pallet_details_function(id):
    pallet_details = await get_pallet_details(id)
    return pallet_details;

@pallet_list_router.get("/possible_pallets")
async def find_possible_pallets_function():
    pallets = await get_possible_pallets()
    return pallets;

@pallet_list_router.get("/new_pallets")
async def find_recent_pallets_function():
    pallets = await get_recent_pallets()
    return pallets

@pallet_list_router.get("/pallet_data")
async def find_pallet_data_function():
    pallet_data = await get_pallet_data()
    return pallet_data;

@pallet_list_router.get("/pallet_summary")
async def find_pallet_summary():
    like = ""
    lot = ""
    product_summary = await get_pallet_summary(like, lot)
    print(product_summary)
    return "pallet_data";

@pallet_list_router.get("/latest_pallet_data")
async def find_latest_pallet_data_function():
    pallet_data = await get_latest_pallet_data()
    return pallet_data;

@pallet_list_router.get("/picklist")
async def find_picklist_function():
    pallet_data = await get_picklist()
    return pallet_data;

@pallet_list_router.get("/data")
async def find_data_function():
    data = await get_data()
    return data;

@pallet_list_router.post("/data/{id}")
async def find_data_for_id_function(id):
    data = await get_data_for_id(id)
    return data;
