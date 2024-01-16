from fastapi import APIRouter, Request
from presentation_layer.pallet_controllers.pallet_crud_controllers import create_pallet, get_pallet, update_pallet, delete_pallet, combine_pallets_import

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
