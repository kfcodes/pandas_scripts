from fastapi import APIRouter, Request
from physical_layer.data_models_layer.object_models import Pallet_group
from business_logic_layer.data_controller_layer.pallet_controllers.pallet_group_crud_controllers import create_new_pallet_group, get_pallet_group_info, update_pallet_group, delete_pallet_group

pallet_group_crud_router = APIRouter();

@pallet_group_crud_router.post("/pallet_group")
async def create_new_pallet_function(body: Request):
    if body:
        body =  await body.json();
        name = body["name"]
        if body["name"] == 0 or body["name"] == None:
            name = "Next";
        else: 
            name = body["name"]
        response = await create_new_pallet_group(name)
        return response;
    else:
        return "Request Body cannot be empty"

@pallet_group_crud_router.get("/pallet_group/{id}")
async def find_pallet_group_function(id):
    pallet_list = await get_pallet_group_info(id)
    return pallet_list

@pallet_group_crud_router.put("/pallet_group/{id}")
async def update_pallet_list(id: int, updated_pallet_group_info: Pallet_group):
    pallet_list = await update_pallet_group(id, updated_pallet_group_info)
    return pallet_list

@pallet_group_crud_router.delete("/pallet_group/{id}")
async def delete_pallet_group_function(id):
    pallet_list = await delete_pallet_group(id)
    return pallet_list
