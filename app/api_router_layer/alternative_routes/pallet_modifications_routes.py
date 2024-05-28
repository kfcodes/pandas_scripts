from fastapi import APIRouter, Request
from data_presentation_layer.data_controller_layer.pallet_controllers.pallet_crud_controllers import combine_pallets_import

combine_pallets_router = APIRouter();

@combine_pallets_router.put("/combine_pallets")
async def combine_function(body: Request):
    if body:
        body =  await body.json();
        pallet_id = int(max(body["pallet_list"]))
        pallet_list = tuple(body["pallet_list"])
        height = int(body["height"])
        response = await combine_pallets_import(pallet_id, height, pallet_list)
        return response
    else:
        return "Request Body cannot be empty"
