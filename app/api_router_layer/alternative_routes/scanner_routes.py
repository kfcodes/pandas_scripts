from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
scanner_router = APIRouter();

from data_presentation_layer.data_controller_layer.scanner_controllers.scanner_controllers import get_all_packing_lists, get_packing_list, get_pallet_info, load_pallet_and_get_packing_list

# SCANNER API ROUTES
@scanner_router.get("/scanner", response_class=HTMLResponse)
async def scanner_packing_lists_function():
    html_data = get_all_packing_lists();
    return HTMLResponse(content=html_data, status_code=200)

@scanner_router.get("/scanner/packing_list/{id}", response_class=HTMLResponse)
async def scanner_packing_list_function(id: int):
    html_data = get_packing_list(id);
    return HTMLResponse(content=html_data, status_code=200)
    
@scanner_router.post("/scanner/pallet_info", response_class=HTMLResponse)
async def scanner_pallet_info_function(request: Request):
    html_data = get_pallet_info(await request.body());
    return HTMLResponse(content=html_data, status_code=200)

@scanner_router.get("/scanner/load_pallet/{id}", response_class=HTMLResponse)
async def load_pallet_function(id: int):
    packing_list_id = await load_pallet_and_get_packing_list(id);
    return RedirectResponse(url=f"/packing_list/{packing_list_id}", status_code=status.HTTP_303_SEE_OTHER)
