from physical_layer.data_access_layer.read_database_functions import get_production_info, get_production_components
from business_logic_layer.external_module_controllers.pdf_logic.create_production_info_pdf import create_production_info_pdf
from business_logic_layer.external_module_controllers.print_logic.print_pdf import print_a4_pdf

import os
from dotenv import load_dotenv
load_dotenv("../.env")

def get_component_data(id):

    try:

        product = f"{os.getenv('PRODUCTIONINFO')}{id}"
        product_info = get_production_info(product)
        uid = product_info[os.getenv("UID")][0]
        production_components = f"{os.getenv('COMPONENTS')}'{uid}'"
        components = get_production_components(production_components);
        pdf_file = create_production_info_pdf(product_info, components);

        print_a4_pdf(pdf_file)

    except Exception as ex:
        print("Data could not be processed: \n", ex)
