from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from presentation_layer.scanner_controllers.scanner_controllers import get_all_packing_lists, get_packing_list, get_pallet_info, load_pallet_and_get_packing_list
from presentation_layer.label_controllers.print_label_controllers import print_large_product_label, print_small_product_label, print_pallet_label
from presentation_layer.product_controllers.product_controllers import get_all_products, get_product_by_id, get_finished_product_by_id, get_all_finished_products
from presentation_layer.assembly_controllers.assembly_information_controllers import get_all_brands, get_products_from_brand, get_assembly_information
from presentation_layer.production_schedule_controllers.production_schedule_controller import get_all_production, get_current_production, get_production_records_by_id
from presentation_layer.pallet_controllers.pallet_crud_controllers import create_pallet, get_pallet, update_pallet, delete_pallet, combine_pallets
from presentation_layer.pallet_controllers.pallet_item_crud_controllers import create_pallet_item_with_id, get_items_on_pallet,get_items_on_pallet , update_pallet_item, delete_pallet_item, get_all_pallet_items, get_new_pallet_items
from presentation_layer.pallet_controllers.pallet_group_controllers import get_all_pallets, get_pallet_group, get_possible_pallets, get_pallet_details, get_data, get_picklist, get_latest_pallet_data, get_pallet_data, get_recent_pallets 
from presentation_layer.finished_product_controllers.finished_product_crud_controllers import create_finished_product, get_finished_product, update_finished_product, delete_finished_product_by_id
from presentation_layer.data_processing_controllers.database_data import process_db_file
from presentation_layer.data_processing_controllers.label_data import process_label_file
from presentation_layer.data_processing_controllers.product_components import process_components_file
from presentation_layer.data_processing_controllers.po_data import process_po_files
from presentation_layer.data_processing_controllers.schedule_data import process_schedule_file

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
@app.get("/print_small_product_label/{id}")
async def print_small_product_label_function_function(id: int):
    await print_small_product_label(id);
    return "PRINTED LABEL"
@app.get("/print_large_product_label/{id}")
async def print_large_product_label_function_function(id: int):
    await print_large_product_label(id);
    return "PRINTED LABEL"
@app.get("/print_pallet_label/{id}")
async def print_pallet_label_function_function(id: int):
    await print_pallet_label(id);
    return "PRINTED LABEL"

# PALLET ROUTES
@app.post("/pallet")
async def create_new_pallet_function():
    pallet_id = await create_pallet()
    return pallet_id
@app.get("/pallet/{id}")
async def find_pallet_function(id):
    pallet = await get_pallet(id)
    return pallet
@app.put("/pallet/{id}")
async def update_pallet_function(id):
    pallet = await update_pallet(id)
    return pallet
@app.delete("/pallet/{id}")
async def delete_pallet_function(id):
    pallet = await delete_pallet(id)
    return pallet
@app.put("/combine_pallets")
async def combine_function():
    response = await combine_pallets()
    return response

# PALLET ITEM ROUTES
@app.post("/pallet_item/{id}")
async def create_pallet_item_function(id):
    item = await create_pallet_item_with_id(id)
    return item
@app.get("/pallet_items/{id}")
async def find_pallet_items_function(id):
    items = await get_items_on_pallet(id)
    return items
@app.put("/pallet_item/{id}")
async def update_pallet_item_function(id):
    item = await update_pallet_item(id)
    return item
@app.delete("/pallet_item/{id}")
async def delete_pallet_item_function(id):
    item = await delete_pallet_item(id)
    return item
@app.get("/new_pallet_items")
async def find_new_pallet_items_function():
    pallet_items = await get_new_pallet_items();
    return pallet_items
@app.get("/all_pallet_items")
async def find_all_pallet_items_function():
    pallet_items = await get_all_pallet_items();
    return pallet_items

# PALLET LIST ROUTES
@app.get("/pallets/{id}")
async def pallet_group_function(id):
    pallets = await get_pallet_group(id)
    return pallets;
@app.get("/all_pallets")
async def find_all_pallets_function():
    pallets = await get_all_pallets()
    return pallets;
@app.get("/pallet_details/{id}")
async def find_pallet_details_function(id):
    details = await get_pallet_details(id)
    return details;
@app.get("/possible_pallets")
async def find_possible_pallets_function():
    pallets = await get_possible_pallets()
    return pallets;
@app.get("/new_pallets")
async def find_recent_pallets_function():
    pallets = await get_recent_pallets()
    return pallets
@app.get("/pallet_data")
async def find_pallet_data_function():
    pallet_data = await get_pallet_data()
    return pallet_data;
@app.get("/latest_pallet_data")
async def find_latest_pallet_data_function():
    pallet_data = await get_latest_pallet_data()
    return pallet_data;
@app.get("/picklist")
async def find_picklist_function():
    pallet_data = await get_picklist()
    return pallet_data;
@app.get("/data")
async def find_data_function():
    data = await get_data()
    return data;

# FINISHED PRODUCTS ROUTES
@app.post("/finished_product")
async def create_new_finished_product_function(request: Request):
    data =  await request.json();
    response = await create_finished_product(data)
    return response;
@app.get("/finished_product/{id}")
async def find_finished_product_function(id):
    finished_product = await get_finished_product_by_id(id)
    return finished_product
@app.put("/finished_product/{id}")
async def update_finished_product_function(id, request: Request):
    data =  await request.json();
    finished_product = await update_finished_product(id, data)
    return finished_product
@app.delete("/finished_product/{id}")
async def delete_finished_product_function(id):
    finished_product = await delete_finished_product_by_id(id)
    return finished_product
@app.get("/finished_products/{id}")
async def finished_product_group_function(group_id):
    finished_products = await get_finished_product_by_id(group_id)
    return finished_products
@app.get("/all_finished_products")
async def find_all_Finished_Products_function():
    return_item = get_all_finished_products()
    return return_item
@app.get("/finished_products/{id}")
async def find_finished_product_by_id_function(id):
    return_item = await get_finished_product_by_id(id)
    return return_item

# PRODUCT ROUTES
@app.get("/products")
async def find_all_products_function():
    return_item = await get_all_products()
    return return_item
@app.get("/products/{id}")
async def find_product_by_id_function(id):
    return_item = await get_product_by_id(id)
    return return_item

# BRAND ROUTES
@app.get("/brands/")
async def find_all_brands_function():
    return_item = await get_all_brands()
    return return_item
@app.get("/brandproducts/{id}")
async def brand_products_function(id):
    return_item = await get_products_from_brand(id)
    return return_item
@app.get("/assembly/{id}")
async def assembly_info_function(id):
    return_item = await get_assembly_information(id)
    return return_item

# PRODUCTION ROUTES
@app.get("/production")
async def find_current_production_function():
    return_item = await get_current_production()
    return return_item;
@app.get("/production/{id}")
async def find_all_production_by_id_function(id):
    return_item = await get_all_production(id)
    return return_item;
@app.get("/production_record/{id}")
async def find_production_record_by_id_function():
    return_item = await get_production_records_by_id(id)
    return return_item;

@app.get("/process_files/process_db_file")
async def process_db_file_function():
    process_db_file()
    return {"message": "files processed"}
@app.get("/process_files/process_label_file")
async def process_label_file_function():
    process_label_file();
    return {"message": "files processed"}
@app.get("/process_files/process_components_file")
async def process_db_components_function():
    process_components_file();
    return {"message": "files processed"}
@app.get("/process_files/process_po_file")
async def process_po_file_function():
    process_po_files();
    return {"message": "files processed"}
@app.get("/process_files/process_schedule_file")
async def process_schedule_file_function():
    process_schedule_file(sheet);
    return {"message": "files processed"}
@app.get("/packing_lists")
async def find_all_packing_lists():
    get_all_packing_lists()
    return {"message": "found packing Lists"}
