from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from presentation_layer.scanner_controllers.get_packing_list_data_controllers import get_all_packing_lists, get_packing_list, get_pallet_info, load_pallet_and_get_packing_list
from presentation_layer.label_controllers.print_label_info import print_large_product_label, print_small_product_label, print_pallet_label
from presentation_layer.product_controllers.product_controllers import get_all_products, get_product_by_id, get_finished_product_by_id, get_all_finished_products

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
    print("Done")

@app.get("/print_large_product_label/{id}", response_class=HTMLResponse)
async def print_large_product_label_function(id: int):
    await print_large_product_label(id);
    print("Done")

@app.get("/print_pallet_label/{id}", response_class=HTMLResponse)
async def print_pallet_label_function(id: int):
    await print_pallet_label(id);
    print("Done")

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


# RETRIEVE ALL proDUCTS
# router.get("/finished_products", ProductDB.findFinishedProducts);
# RETRIEVE A SINGLE PRODUCT WITH PRODUCTID
# router.get("/product/:id", ProductDB.findOne);
# router.get("/finished_products/:id", ProductDB.findOneFinishedProduct);

