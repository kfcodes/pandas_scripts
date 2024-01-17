from fastapi import APIRouter, Request
from presentation_layer.finished_product_controllers.finished_product_crud_controllers import create_finished_product, get_finished_product, update_finished_product, delete_finished_product_by_id

finished_product_router = APIRouter();

@finished_product_router.post("/finished_product")
async def create_new_finished_product_function(request: Request):
    data =  await request.json();
    response = await create_finished_product(data)
    return response;

@finished_product_router.get("/finished_product/{id}")
async def find_finished_product_function(id):
    finished_product = await get_finished_product(id)
    return finished_product

@finished_product_router.put("/finished_product/{id}")
async def update_finished_product_function(id, request: Request):
    data =  await request.json();
    finished_product = await update_finished_product(id, data)
    return finished_product

@finished_product_router.delete("/finished_product/{id}")
async def delete_finished_product_function(id):
    finished_product = await delete_finished_product_by_id(id)
    return finished_product
