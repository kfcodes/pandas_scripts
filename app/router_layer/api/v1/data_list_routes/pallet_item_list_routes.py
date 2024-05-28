from fastapi import APIRouter
from business_logic_layer.data_controller_layer.pallet_controllers.pallet_item_list_controllers import get_all_pallet_items, get_new_pallet_items, find_pallet_items_for_pallet_function

pallet_item_list_router = APIRouter();

@pallet_item_list_router.get("/all_pallet_items")
async def find_all_pallet_items_function():
    pallet_items = await get_all_pallet_items();
    return pallet_items

@pallet_item_list_router.get("/new_pallet_items")
async def find_new_pallet_items_function():
    pallet_items = await get_new_pallet_items();
    return pallet_items

@pallet_item_list_router.get("/pallet_items/{id}")
async def find_pallet_items_for_function(id):
    pallet_items = await find_pallet_items_for_pallet_function(id);
    return pallet_items
