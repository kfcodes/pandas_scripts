from fastapi import APIRouter, Request
from presentation_layer.data_controller_layer.label_controllers.print_label_controllers import print_large_product_label, print_small_product_label, print_pallet_label, print_combined_pallet_label, print_blank_pallet_label, get_label_info

label_router = APIRouter();

# LABEL PRINTER API ROUTES
@label_router.get("/print_small_product_label/{id}")
async def print_small_product_label_function(id: int):
    response = await print_small_product_label(id);
    return response;

@label_router.post("/print_large_product_label/{id}")
async def print_large_product_label_function(id: int, body: Request):
    if body:
        body =  await body.json();
        quantity = int(body["qty"])
        exp = str(body["exp"])
        # exp = "260218"
        if body["qtyPerBox"] == 0 or body["qtyPerBox"] == None:
            quantity_in_a_box = 0;
        else: 
            quantity_in_a_box = int(body["qtyPerBox"])
        response = await print_large_product_label(id, quantity, quantity_in_a_box, exp);
        return response;
    else:
        return "Request Body cannot be empty"

@label_router.post("/print_large_combined_label")
async def print_large_combined_label_function(data: Request):
    json_data =  await data.json();
    response = await print_combined_pallet_label(json_data);
    return response;

@label_router.post("/print_blank_labels")
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
