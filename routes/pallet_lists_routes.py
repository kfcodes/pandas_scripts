from fastapi import APIRouter


pallet_item_crud_router = APIRouter();

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
    pallet_details = await get_pallet_details(id)
    return pallet_details;
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
@app.post("/data/{id}")
async def find_data_for_id_function(id):
    data = await get_data_for_id(id)
    return data;
