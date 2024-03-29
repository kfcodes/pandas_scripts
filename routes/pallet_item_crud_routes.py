from fastapi import APIRouter
from data_models_layer.object_models import Pallet_item
from presentation_layer.pallet_controllers.pallet_item_crud_controllers import create_pallet_item_with_id, get_items_on_pallet,get_items_on_pallet , update_pallet_item, delete_pallet_item

pallet_item_crud_router = APIRouter();

@pallet_item_crud_router.post("/pallet_item/{id}")
async def create_pallet_item_function(id):
    item = await create_pallet_item_with_id(id)
    return item

@pallet_item_crud_router.get("/pallet_items/{id}")
async def find_pallet_items_function(id):
    items = await get_items_on_pallet(id)
    return items

@pallet_item_crud_router.put("/pallet_item/{id}")
async def update_pallet_item_function(id: int, updated_pallet_item_info: Pallet_item):
    updated_item = await update_pallet_item(id, updated_pallet_item_info)
    return updated_item

@pallet_item_crud_router.delete("/pallet_item/{id}")
async def delete_pallet_item_function(id):
    item = await delete_pallet_item(id)
    return item
