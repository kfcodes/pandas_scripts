from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from presentation_layer.scanner_controllers.get_packing_list_data_controllers import get_all_packing_lists, get_packing_list, get_pallet_info, load_pallet_and_get_packing_list
from presentation_layer.label_controllers.print_label_info import print_large_product_label, print_small_product_label, print_pallet_label
from presentation_layer.product_controllers.product_controllers import get_all_products, get_product_by_id, get_finished_product_by_id, get_all_finished_products
from presentation_layer.brand_controllers.brand_controller import get_all_brands, get_products_from_brand, get_product_components
from presentation_layer.production_schedule_controllers.production_schedule_controller import get_all_production, get_current_production, get_production_records_by_id
from presentation_layer.pallet_controllers.pallet_controllers import create_pallet, get_pallet_by_id, update_pallet_by_id, delete_pallet_by_id, get_pallet_group, get_all_pallets

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
async def scanner_packing_lists():
    html_data = get_all_packing_lists();
    return HTMLResponse(content=html_data, status_code=200)
@app.get("/scanner/packing_list/{id}", response_class=HTMLResponse)
async def scanner_packing_list(id: int):
    html_data = get_packing_list(id);
    return HTMLResponse(content=html_data, status_code=200)
@app.post("/scanner/pallet_info", response_class=HTMLResponse)
async def scanner_pallet_info(request: Request):
    html_data = get_pallet_info(await request.body());
    return HTMLResponse(content=html_data, status_code=200)
@app.get("/scanner/load_pallet/{id}", response_class=HTMLResponse)
async def load_pallet(id: int):
    packing_list_id = await load_pallet_and_get_packing_list(id);
    return RedirectResponse(url=f"/packing_list/{packing_list_id}", status_code=status.HTTP_303_SEE_OTHER)

# LABEL PRINTER API ROUTES
@app.get("/print_small_product_label/{id}", response_class=HTMLResponse)
async def print_small_product_label_function(id: int):
    await print_small_product_label(id);
    print("PRINTED LABEL")
@app.get("/print_large_product_label/{id}", response_class=HTMLResponse)
async def print_large_product_label_function(id: int):
    await print_large_product_label(id);
    print("PRINTED LABEL")
@app.get("/print_pallet_label/{id}", response_class=HTMLResponse)
async def print_pallet_label_function(id: int):
    await print_pallet_label(id);
    print("PRINTED LABEL")

# PRODUCT ROUTES
@app.get("/products")
async def find_all_products():
    return_item = await get_all_products()
    return JSONResponse(content=return_item)
@app.get("/products/{id}")
async def find_product_by_id(id):
    return_item = await get_product_by_id(id)
    return JSONResponse(content=return_item)
@app.get("/finished_products")
async def find_all_Finished_Products():
    return_item = get_all_finished_products()
    return JSONResponse(content=return_item)
@app.get("/finished_products/{id}")
async def find_finished_product_by_id(id):
    return_item = await get_finished_product_by_id(id)
    return JSONResponse(content=return_item)

# BRAND ROUTES
@app.get("/brands/")
async def find_all_brands():
    return_item = await get_all_brands()
    return JSONResponse(content=return_item)
@app.get("/brandproducts/{id}")
async def brand_products(id):
    return_item = await get_products_from_brand(id)
    return JSONResponse(content=return_item)
@app.get("/components/{id}")
async def product_components(id):
    return_item = await get_product_components(id)
    return JSONResponse(content=return_item)

# PRODUCTION ROUTES
@app.get("/production")
async def find_current_production():
    return_item = await get_current_production()
    return JSONResponse(content=return_item)
@app.get("/all_production/{id}")
async def find_all_production_by_id(id):
    return_item = await get_all_production(id)
    return JSONResponse(content=return_item)
@app.get("/production/{id}")
async def find_production_record_by_id():
    return_item = await get_production_records_by_id(id)
    return JSONResponse(content=return_item)

# PALLET ROUTES
@app.post("/pallet")
async def create_pallet():
    pallet_id = await create_pallet()
    return JSONResponse(content=pallet_id)
@app.get("/pallet/{id}")
async def find_pallet():
    pallet = await get_pallet_by_id(id)
    return JSONResponse(content=pallet)
@app.put("/pallet/{id}")
async def update_pallet():
    pallet = await update_pallet_by_id(id)
    return JSONResponse(content=pallet)
@app.delete("/pallet/{id}")
async def delete_pallet():
    pallet = await delete_pallet_by_id(id)
    return JSONResponse(content=pallet)
@app.get("/pallets/{id}")
async def pallet_group():
    pallets = await get_pallet_group(id)
    return JSONResponse(content=pallets)
@app.get("/all_pallets")
async def find_all_pallets():
    pallets = await get_all_pallets()
    return JSONResponse(content=pallets)
