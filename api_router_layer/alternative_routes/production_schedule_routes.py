from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse

from presentation_layer.data_controller_layer.production_schedule_controllers.production_schedule_controller import get_all_production, get_current_production, get_production_records_by_id

schedule_router = APIRouter();

@schedule_router.get("/production")
async def find_current_production_function():
    return_item = await get_current_production()
    return return_item;

@schedule_router.get("/production/{id}")
async def find_all_production_by_id_function(id):
    return_item = await get_all_production(id)
    return return_item;

@schedule_router.get("/production_record/{id}")
async def find_production_record_by_id_function():
    return_item = await get_production_records_by_id(id)
    return return_item;
