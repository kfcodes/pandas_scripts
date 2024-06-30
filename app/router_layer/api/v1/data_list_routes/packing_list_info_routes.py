from fastapi import APIRouter
from business_logic_layer.data_controller_layer.pallet_controllers.pallet_group_controllers import get_open_pallet_groups, get_open_pallets, get_packing_list_pallets

packing_list_data_router = APIRouter();

# GET ALL OPEN PACKING_LISTS SUMMARY INFORMATION
@packing_list_data_router.get("/open_packing_lists")
async def get_all_open_packing_lists_summary_information():
    packing_lists = await open_packing_lists_summary()
    return packing_lists;

# GET NAMES OF OPEN PACKING LISTS
@packing_list_data_router.get("/open_packing_list_names")
async def get_all_open_packing_list_names():
    packing_lists = await open_packing_lists_summary()
    return packing_lists;

# GET PALLETS NOT ASSIGNED A PACKING LIST
@packing_list_data_router.get("/open_pallets")
async def find_open_pallets_information():
    pallets = await get_open_pallets()
    return pallets;

# GET INFORMATION FOR PALLETS ON A PERTICULAR PACKING LIST
@packing_list_data_router.get("/packing_list_pallets/{id}")
async def find_packing_list_pallets_function():
    pallets = await get_packing_list_pallets()
    return pallets;
