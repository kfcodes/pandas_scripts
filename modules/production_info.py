import sys
import os
from dotenv import load_dotenv
load_dotenv("../.env")
import pandas as pd
from database.read_db_index import get_production_documentation, get_product_components
# from pdf.create_production_info_pdf import create_production_info_pdf
# from print.print_pdf import print_a4_pdf

id = str(sys.argv[1])
selection = f"{os.getenv('PRODUCTIONINFO')}{id}"
info = get_production_documentation(selection)
print(info)
# components = get_product_components(product_id);
# pdf_file = create_production_info_pdf(info, components);
# print_a4_pdf(pdf_file)
