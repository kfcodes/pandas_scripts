from fastapi import APIRouter, Request
from physical_layer.data_models_layer.object_models import Pallet_group
from business_logic_layer.data_controller_layer.packing_list_controllers.packing_list_crud_controllers import create_new_packing_list, get_packing_list_info, update_packing_list_name, delete_packing_list, dispatch_packing_list

packing_list_crud_router = APIRouter();

# CREATE A PACKING LIST USING NAME
@packing_list_crud_router.post("/packing_list/create/{name}")
async def create_new_packing_list_function(name: str):
    # if body:
    #     body =  await body.json();
    #     name = body["name"]
    #     if body["name"] == 0 or body["name"] == None or body["name"] == "":
    #         name = "Next";
    #     else: 
    #         name = body["name"]
    response = await create_new_packing_list(name)
    return response;
    # else:
    #     return "Request Body cannot be empty"

# GET PACKING LIST SUMARY INFO
@packing_list_crud_router.get("/packing_list/summary/{id}")
async def find_summary_info_for_packing_list(id):
    packing_list_info = await get_packing_list_info(id)
    return packing_list_info

# UPDATE PACKING LIST NAME
@packing_list_crud_router.put("/packing_list/update/{id}/{name}")
async def update_packing_list_name_route(id: int, name: str):
    packing_list_info = await update_packing_list_name(id, name)
    return packing_list_info

# MARK PACKING LIST AS DISPATCHED
@packing_list_crud_router.put("/packing_list/dispatch/{id}")
async def mark_packing_list_as_dispatched(id: int):
    pallet_list = await dispatch_packing_list(id)
    return pallet_list

# DELETE A PACKING LIST
@packing_list_crud_router.delete("/packing_list/delete/{id}")
async def delete_a_packing_list(id):
    pallet_list = await delete_packing_list(id)
    return pallet_list
