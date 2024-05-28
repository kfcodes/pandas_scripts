from fastapi import APIRouter
from business_logic_layer.data_controller_layer.certificate_controllers.certificate_data_controllers import create_and_print_certificate

cert_router = APIRouter();

@cert_router.post("/print_cert/{id}")
async def print_cert_function(id: int):
    response = await create_and_print_certificate(id);
    return response
