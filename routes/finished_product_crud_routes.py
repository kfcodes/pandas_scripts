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
