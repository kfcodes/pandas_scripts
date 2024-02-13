from fastapi import APIRouter, Request
from presentation_layer.label_controllers.print_label_controllers import print_large_product_label, print_small_product_label, print_pallet_label, print_combined_pallet_label, print_blank_pallet_label, get_label_info

label_router = APIRouter();

# LABEL PRINTER API ROUTES
@label_router.get("/print_small_product_label/{id}")
async def print_small_product_label_function(id: int):
    response = await print_small_product_label(id);
    return response;

@label_router.post("/print_large_product_label/{id}")
async def print_large_product_label_function(id: int, body: Request):
    # if body:
    #     body =  await body.json();
    #     quantity = int(body["quantity"])
    #     response = await print_large_product_label(id, quantity);
    #     return response;
    # else:
    response = await print_large_product_label(id, 1);
    return "No Quantity", response

@label_router.post("/print_large_combined_label")
async def print_large_combined_label_function(data: Request):
    json_data =  await data.json();
    response = await print_combined_pallet_label(json_data);
    return response;

@label_router.get("/print_blank_labels")
async def print_blank_label_function():
    response = await print_blank_pallet_label();
    return response;

@label_router.get("/label/{id}")
async def print_pallet_label_function_function(id: int):
    response = await print_pallet_label(id);
    return response

@label_router.get("/label_info/{id}")
async def label_info_function(id: str):
    response = await get_label_info(id);
    return response
