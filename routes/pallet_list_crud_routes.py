from fastapi import APIRouter
from data_models_layer.object_models import Pallet_list
from presentation_layer.pallet_list_controllers.pallet_crud_controllers import create_pallet,_list get_pallet_list, update_pallet_list, delete_pallet_list

pallet_list_crud_router = APIRouter();

@pallet_list_crud_router.post("/pallet_list")
async def create_new_pallet_function():
    pallet_list_id = await create_pallet_list()
    return pallet_list_id

@pallet_list_crud_router.get("/pallet_list/{id}")
async def find_pallet_list_function(id):
    pallet_list = await get_pallet_list(id)
    return pallet_list

@pallet_list_crud_router.put("/pallet_list/{id}")
async def update_pallet_list_function(id: int, updated_pallet_info: Pallet):
    pallet_list = await update_pallet_list(id, updated_pallet_info)
    return pallet_list

@pallet_list_crud_router.delete("/pallet/{id}")
async def delete_pallet_list_function(id):
    pallet_list = await delete_pallet_list(id)
    return pallet_list
