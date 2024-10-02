from fastapi import APIRouter
from business_logic_layer.data_controller_layer.packing_list_controllers.packing_list_controllers import get_open_packing_lists, get_open_packing_list_names, get_pallets_not_on_a_packing_list, get_packing_list_pallets, get_packing_list_summary_information, get_picklist_status_information
from fastapi import APIRouter, Request
from business_logic_layer.data_controller_layer.packing_list_controllers.packing_list_controllers import get_open_packing_lists, get_open_packing_list_names, get_pallets_not_on_a_packing_list, get_packing_list_summary_information, get_picklist_status_information, set_pallet_packing_list, get_packing_list_pallet_information

packing_list_data_router = APIRouter();

# GET ALL OPEN PACKING_LISTS SUMMARY INFORMATION
@packing_list_data_router.get("/open_packing_lists")
async def get_all_open_packing_lists_summary_information():
    packing_lists = await get_open_packing_lists()
    return packing_lists;

# GET NAMES FOR OPEN PACKING LISTS
@packing_list_data_router.get("/open_packing_list_names")
async def get_all_open_packing_list_names():
    packing_lists = await get_open_packing_list_names()
    return packing_lists;

# GET PALLETS NOT ASSIGNED A PACKING LIST
@packing_list_data_router.get("/open_pallets")
async def find_pallets_not_assigned_to_paking_list_information():
    pallets = await get_pallets_not_on_a_packing_list()
    return pallets;

# GET PACKING LIST SUMMARY INFORMATION
@packing_list_data_router.get("/packing_list_summary/{id}")
async def find_packing_list_summary_information(id: int):
    pallets = await get_packing_list_summary_information(id)
    return pallets;

# GET PICKLIST STATUS INFORMATION
@packing_list_data_router.get("/picklist_status/{id}")
async def find_picklist_status_information(id: int):
    pallets = await get_picklist_status_information(id)
    return pallets;

# UPDATE PACKING LIST FOR PALLET
@packing_list_data_router.put("/set_pallet_packing_list/")
async def set_pallet_packing_list_function(request: Request):
    data =  await request.json();
    updated_pallet = await set_pallet_packing_list(data)
    return updated_pallet;

# GET PACKING LIST PALLET INFORMATION
@packing_list_data_router.get("/packing_list_pallets/{id}")
async def find_packing_list_pallet_information(id: int):
    pallets_info = await get_packing_list_pallet_information(id)
    return pallets_info;
