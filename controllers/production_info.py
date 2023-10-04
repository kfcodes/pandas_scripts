import os
from dotenv import load_dotenv
from modules.database.read_db_index import get_production_info, get_production_components
from modules.pdf.create_production_info_pdf import create_production_info_pdf
from modules.print.print_pdf import print_a4_pdf

load_dotenv(".env")

def get_component_data(id):
    try:
        product = f"{os.getenv('PRODUCTIONINFO')}{id}"
        le_product_info = get_production_info(product)
        uid = le_product_info[os.getenv("UID")][0]
        le_production_components = f"{os.getenv('COMPONENTS')}'{uid}'"
        le_components = get_production_components(le_production_components);
        pdf_file = create_production_info_pdf(le_product_info, le_components);
        print_a4_pdf(pdf_file)

    except Exception as ex:
        print("Data could not be processed: \n", ex)
