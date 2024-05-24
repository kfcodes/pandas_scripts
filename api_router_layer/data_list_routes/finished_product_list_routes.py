from fastapi import APIRouter
from presentation_layer.data_controller_layer.product_controllers.product_controllers import get_all_products, get_product_by_id, get_finished_product_by_id, get_all_finished_products

finished_product_list_router = APIRouter();

@finished_product_list_router.get("/finished_products/{id}")
async def finished_product_group_function(group_id):
    finished_products = await get_finished_product_by_id(group_id)
    return finished_products

@finished_product_list_router.get("/all_finished_products")
async def find_all_Finished_Products_function():
    return_item = get_all_finished_products()
    return return_item

@finished_product_list_router.get("/finished_products/{id}")
async def find_finished_product_by_id_function(id):
    return_item = await get_finished_product_by_id(id)
    return return_item

@finished_product_list_router.get("/products")
async def find_all_products_function():
    return_item = await get_all_products()
    return return_item

@finished_product_list_router.get("/products/{id}")
async def find_product_by_id_function(id):
    return_item = await get_product_by_id(id)
    return return_item
