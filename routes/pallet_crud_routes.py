from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
scanner_router = APIRouter();

from presentation_layer.pallet_controllers.pallet_crud_controllers import create_pallet, get_pallet, update_pallet, delete_pallet, combine_pallets_import
from presentation_layer.pallet_controllers.pallet_item_crud_controllers import create_pallet_item_with_id, get_items_on_pallet,get_items_on_pallet , update_pallet_item, delete_pallet_item, get_all_pallet_items, get_new_pallet_items
from presentation_layer.pallet_controllers.pallet_group_controllers import get_all_pallets, get_pallet_group, get_possible_pallets, get_pallet_details, get_data, get_picklist, get_latest_pallet_data, get_pallet_data, get_recent_pallets, get_data_for_id

pallet_crud_router = APIRouter();

@pallet_crud_router.post("/pallet")
async def create_new_pallet_function():
    pallet_id = await create_pallet()
    return pallet_id

@pallet_crud_router.get("/pallet/{id}")
async def find_pallet_function(id):
    pallet = await get_pallet(id)
    return pallet

@pallet_crud_router.put("/pallet/{id}")
async def update_pallet_function(id: int, request: Request):
    data =  await request.json();
    pallet = await update_pallet(id, data)
    return pallet

@pallet_crud_router.delete("/pallet/{id}")
async def delete_pallet_function(id):
    pallet = await delete_pallet(id)
    return pallet
