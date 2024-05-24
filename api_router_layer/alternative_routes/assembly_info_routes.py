from fastapi import APIRouter, Request
from presentation_layer.data_controller_layer.assembly_controllers.assembly_information_controllers import get_all_brands, get_products_from_brand, get_assembly_information

assembly_router = APIRouter();

@assembly_router.get("/brands/")
async def find_all_brands_function():
    return_item = await get_all_brands()
    return return_item

@assembly_router.get("/brandproducts/{id}")
async def brand_products_function(id):
    return_item = await get_products_from_brand(id)
    return return_item

@assembly_router.get("/assembly/{id}")
async def assembly_info_function(id):
    # return_item = await get_assembly_information(id)
    return_item = "Got Data"
    return return_item
