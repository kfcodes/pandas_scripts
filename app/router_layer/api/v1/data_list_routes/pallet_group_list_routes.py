from fastapi import APIRouter
from business_logic_layer.data_controller_layer.pallet_controllers.pallet_group_controllers import get_open_pallet_groups, get_open_pallets, get_packing_list_pallets

pallet_group_data_router = APIRouter();

# GET ALL PACKING_LISTS NOT DISPATCHED
@pallet_group_data_router.get("/open_packing_lists")
async def find_open_pallet_groups_function():
    pallet_group_list = await get_open_pallet_groups()
    return pallet_group_list;

# GET ALL PALLETS NOT ASSIGNED A PACKING LIST
@pallet_group_data_router.get("/open_pallets")
async def find_open_pallets_function():
    pallets = await get_open_pallets()
    return pallets;

# GET INFORMATION FOR PALLETS ON A PERTICULAR PACKING LIST
@pallet_group_data_router.get("/packing_list_pallets/{id}")
async def find_packing_list_pallets_function():
    pallets = await get_packing_list_pallets()
    return pallets;
