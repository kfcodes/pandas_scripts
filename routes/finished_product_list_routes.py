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
