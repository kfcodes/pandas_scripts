from fastapi import APIRouter
from business_logic_layer.data_controller_layer.pallet_controllers.pallet_group_controllers import get_open_pallet_groups

pallet_group_crud_router = APIRouter();

@pallet_group_crud_router.get("/open_packing_lists")
async def find_open_pallet_groups_function():
    pallet_group_list = await get_open_pallet_groups()
    return pallet_group_list;
