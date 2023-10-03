import os
from dotenv import load_dotenv
load_dotenv(".env")
from database.read_db_index import get_production_info, get_production_components
from pdf.create_production_info_pdf import create_production_info_pdf
from print.print_pdf import print_a4_pdf

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
