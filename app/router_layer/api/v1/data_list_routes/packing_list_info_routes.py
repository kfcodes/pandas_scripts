from fastapi import APIRouter
from business_logic_layer.data_controller_layer.packing_list_controllers.packing_list_controllers import get_open_packing_lists, get_open_packing_list_names, get_pallets_not_on_a_packing_list, get_packing_list_pallets

packing_list_data_router = APIRouter();

# GET ALL OPEN PACKING_LISTS SUMMARY INFORMATION
@packing_list_data_router.get("/open_packing_lists")
async def get_all_open_packing_lists_summary_information():
    packing_lists = await get_open_packing_lists()
    return packing_lists;

# GET NAMES OF OPEN PACKING LISTS
@packing_list_data_router.get("/open_packing_list_names")
async def get_all_open_packing_list_names():
    packing_lists = await get_open_packing_list_names()
    return packing_lists;

# GET PALLETS NOT ASSIGNED A PACKING LIST
@packing_list_data_router.get("/open_pallets")
async def find_open_pallets_information():
    pallets = await get_pallets_not_on_a_packing_list()
    return pallets;

# GET INFORMATION FOR PALLETS ON A PERTICULAR PACKING LIST
@packing_list_data_router.get("/packing_list_pallets/{id}")
async def find_packing_list_pallets_function(id: int):
    pallets = await get_packing_list_pallets(id)
    return pallets;
