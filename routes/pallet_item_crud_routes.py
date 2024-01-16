from fastapi import APIRouter
scanner_router = APIRouter();
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
