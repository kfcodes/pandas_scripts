from fastapi import APIRouter
from presentation_layer.pallet_controllers.pallet_item_list_controllers import get_all_pallet_items, get_new_pallet_items

pallet_item_list_router = APIRouter();

@pallet_item_list_router.get("/new_pallet_items")
async def find_new_pallet_items_function():
    pallet_items = await get_new_pallet_items();
    return pallet_items

@pallet_item_list_router.get("/all_pallet_items")
async def find_all_pallet_items_function():
    pallet_items = await get_all_pallet_items();
    return pallet_items
