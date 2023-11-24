from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from presentation_layer.scanner_controllers.get_packing_list_data_controllers import get_all_packing_lists, get_packing_list, get_pallet_info, load_pallet_and_get_packing_list
from presentation_layer.label_controllers.print_label_info import print_large_product_label, print_small_product_label, print_pallet_label
from presentation_layer.product_controllers.product_controllers import get_all_products, get_product_by_id, get_finished_product_by_id, get_all_finished_products
from presentation_layer.brand_controllers.brand_controller import get_all_brands, get_products_from_brand, get_assembly_information
from presentation_layer.production_schedule_controllers.production_schedule_controller import get_all_production, get_current_production, get_production_records_by_id
from presentation_layer.pallet_controllers.pallet_crud_controllers import create_pallet, get_pallet, update_pallet, delete_pallet, combine_pallets
from presentation_layer.pallet_controllers.pallet_item_crud_controllers import create_pallet_item_with_id, get_items_on_pallet,get_all_pallet_items , update_pallet_item_by_id, delete_pallet_item_by_id
from presentation_layer.pallet_controllers.pallet_group_controllers import get_all_pallets, get_pallet_group, get_possible_pallets, get_pallet_details, get_data, get_picklist, get_latest_pallet_data, get_pallet_data, get_recent_pallets 
from presentation_layer.finished_product_controllers.finished_product_controllers import create_finished_product, get_finished_product_by_id, update_finished_product_by_id, delete_finished_product_by_id, get_finished_product_group

import os
from dotenv import load_dotenv
load_dotenv(".env")

sheet = os.getenv("SHEETINPUT");

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# SCANNER API ROUTES
@app.get("/scanner", response_class=HTMLResponse)
async def scanner_packing_lists_function():
    html_data = get_all_packing_lists();
    return HTMLResponse(content=html_data, status_code=200)
@app.get("/scanner/packing_list/{id}", response_class=HTMLResponse)
async def scanner_packing_list_function(id: int):
    html_data = get_packing_list(id);
    return HTMLResponse(content=html_data, status_code=200)
@app.post("/scanner/pallet_info", response_class=HTMLResponse)
async def scanner_pallet_info_function(request: Request):
    html_data = get_pallet_info(await request.body());
    return HTMLResponse(content=html_data, status_code=200)
@app.get("/scanner/load_pallet/{id}", response_class=HTMLResponse)
async def load_pallet_function(id: int):
    packing_list_id = await load_pallet_and_get_packing_list(id);
    return RedirectResponse(url=f"/packing_list/{packing_list_id}", status_code=status.HTTP_303_SEE_OTHER)

# LABEL PRINTER API ROUTES
@app.get("/print_small_product_label/{id}", response_class=HTMLResponse)
async def print_small_product_label_function_function(id: int):
    await print_small_product_label(id);
    print("PRINTED LABEL")
@app.get("/print_large_product_label/{id}", response_class=HTMLResponse)
async def print_large_product_label_function_function(id: int):
    await print_large_product_label(id);
    print("PRINTED LABEL")
@app.get("/print_pallet_label/{id}", response_class=HTMLResponse)
async def print_pallet_label_function_function(id: int):
    await print_pallet_label(id);
    print("PRINTED LABEL")

# PRODUCT ROUTES
@app.get("/products")
async def find_all_products_function():
    return_item = await get_all_products()
    return JSONResponse(content=return_item)
@app.get("/products/{id}")
async def find_product_by_id_function(id):
    return_item = await get_product_by_id(id)
    return JSONResponse(content=return_item)
@app.get("/finished_products")
async def find_all_Finished_Products_function():
    return_item = get_all_finished_products()
    return JSONResponse(content=return_item)
@app.get("/finished_products/{id}")
async def find_finished_product_by_id_function(id):
    return_item = await get_finished_product_by_id(id)
    return JSONResponse(content=return_item)

# BRAND ROUTES
@app.get("/brands/")
async def find_all_brands_function():
    return_item = await get_all_brands()
    return JSONResponse(content=return_item)
@app.get("/brandproducts/{id}")
async def brand_products_function(id):
    return_item = await get_products_from_brand(id)
    return JSONResponse(content=return_item)
@app.get("/assembly/{id}")
async def assembly_info_function(id):
    return_item = await get_assembly_information(id)
    return JSONResponse(content=return_item)

# PRODUCTION ROUTES
@app.get("/production")
async def find_current_production_function():
    return_item = await get_current_production()
    return JSONResponse(content=return_item)
@app.get("/production/{id}")
async def find_all_production_by_id_function(id):
    return_item = await get_all_production(id)
    return JSONResponse(content=return_item)
@app.get("/production_record/{id}")
async def find_production_record_by_id_function():
    return_item = await get_production_records_by_id(id)
    return JSONResponse(content=return_item)

# PALLET ROUTES
@app.post("/pallet")
async def create_new_pallet_function():
    pallet_id = await create_pallet()
    return pallet_id
@app.get("/pallet/{id}")
async def find_pallet_function():
    pallet = await get_pallet(id)
    return JSONResponse(content=pallet)
@app.put("/pallet/{id}")
async def update_pallet_function():
    pallet = await update_pallet(id)
    return JSONResponse(content=pallet)
@app.delete("/pallet/{id}")
async def delete_pallet_function():
    pallet = await delete_pallet(id)
    return JSONResponse(content=pallet)
@app.get("/pallets/{id}")
async def pallet_group_function():
    pallets = await get_pallet_group(id)
    return JSONResponse(content=pallets)
@app.put("/combine_pallets")
async def combine_function():
    response = await combine_pallets()
    return JSONResponse(content=response)
# PALLET ITEM ROUTES
@app.post("/pallet_item/{id}")
async def create_pallet_item_function(id):
    return_item = await create_pallet_item_with_id(id)
    return JSONResponse(content=return_item)
@app.get("/pallet_items/{id}")
async def find_pallet_items_function(id):
    items = await get_items_on_pallet(id)
    return JSONResponse(content=items)
@app.put("/pallet_item/{id}")
async def update_pallet_item_function(id):
    return_item = await update_pallet_item_by_id(id)
    return JSONResponse(content=return_item)
@app.delete("/pallet_item/{id}")
async def delete_pallet_item_function(id):
    return_item = await delete_pallet_item_by_id(id)
    return JSONResponse(content=return_item)
@app.get("/pallet_items")
async def find_all_pallet_items_function():
    pallet_items = await get_all_pallet_items(id)
    return JSONResponse(content=pallet_items)

# PALLET LIST ROUTES
@app.get("/all_pallets")
async def find_all_pallets_function():
    pallets = await get_all_pallets()
    return JSONResponse(content=pallets)
@app.get("/pallet_details/{id}")
async def find_pallet_details_function(id):
    details = await get_pallet_details(id)
    return JSONResponse(content=details)
@app.get("/possible_pallets")
async def find_possible_pallets_function():
    pallets = await get_possible_pallets()
    return JSONResponse(content=pallets)
@app.get("/pallets")
async def find_recent_pallets_function():
    pallets = await get_recent_pallets()
    return JSONResponse(content=pallets)
@app.get("/pallet_data")
async def find_pallet_data_function():
    pallet_data = await get_pallet_data()
    return JSONResponse(content=pallet_data)
@app.get("/latest_pallet_data")
async def find_latest_pallet_data_function():
    pallet_data = await get_latest_pallet_data()
    return JSONResponse(content=pallet_data)
@app.get("/picklist")
async def find_picklist_function():
    pallet_data = await get_picklist()
    return JSONResponse(content=pallet_data)
@app.get("/data")
async def find_data_function():
    data = await get_data()
    return JSONResponse(content=data)

# FINISHED PRODUCTS ROUTES
@app.post("/finished_product")
async def create_new_finished_product_function():
    finished_product_id = await create_finished_product()
    return JSONResponse(content=finished_product_id)
@app.get("/finished_product/{id}")
async def find_finished_product_function(id):
    finished_product = await get_finished_product_by_id(id)
    return JSONResponse(content=finished_product)
@app.put("/finished_product/{id}")
async def update_finished_product_function(id):
    finished_product = await update_finished_product_by_id(id)
    return JSONResponse(content=finished_product)
@app.delete("/finished_product/{id}")
async def delete_finished_product_function(id):
    finished_product = await delete_finished_product_by_id(id)
    return JSONResponse(content=finished_product)
@app.get("/finished_products/{id}")
async def finished_product_group_function(group_id):
    finished_products = await get_finished_product_group(group_id)
    return JSONResponse(content=finished_products)
