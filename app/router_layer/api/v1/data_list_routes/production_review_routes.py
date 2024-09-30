from fastapi import APIRouter, Request
from business_logic_layer.data_controller_layer.production_overview_controllers.production_review_controllers import get_production_review_information

production_review_router = APIRouter();

# GET PRODUCTION SUMMARY INFORMATION
@production_review_router.get("/production_review")
async def production_review_information():
    production_review_array = await get_production_review_information()
    return production_review_array;

