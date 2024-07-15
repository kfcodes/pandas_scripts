from fastapi import APIRouter, Request
from business_logic_layer.data_controller_layer.certificate_controllers.certificate_data_controllers import print_pdf_cert_for_packing_list

pdf_router = APIRouter();

@pdf_router.post("/certificate_pdf/{id}")
async def print_pdf_certificate_report(id: int):
        response = await print_pdf_cert_for_packing_list(id);
        return response;
