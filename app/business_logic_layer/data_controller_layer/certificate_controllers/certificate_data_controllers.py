from physical_layer.data_access_layer.read_database_functions import read_to_list_index
from business_logic_layer.external_module_controllers.pdf_logic.create_certificate_pdf import create_certificate_pdf 
# from business_logic_layer.external_module_controllers.print_logic.print_pdf import print_a4_pdf 

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

async def print_pdf_cert_for_packing_list(id):
    try:
        data = read_to_list_index(f"{os.getenv('GETCERTIFICATEDATA')}{int(id)}")
        pdf_data_file = create_certificate_pdf(data)
        response = print_a4_pdf(pdf_data_file)
        return response
    except Exception as ex:
        print("Data could not be processed: \n", ex)

