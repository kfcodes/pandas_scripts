from fastapi import APIRouter, Request

from presentation_layer.pallet_controllers.pallet_crud_controllers import combine_pallets_import

combine_pallets_router = APIRouter();

# @combine_pallets_router.post("/combine_pallets")
# async def combine_function(pallet_list:list,height:int):
#     response = await combine_pallets_import(pallet_list, height)
#     return response
