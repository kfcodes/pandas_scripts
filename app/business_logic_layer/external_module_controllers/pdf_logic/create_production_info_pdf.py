from fpdf import FPDF

import os
from dotenv import load_dotenv
load_dotenv("../../.server_config_files/fastAPI.env")

def create_production_info_pdf(finished_product, product_components):
    try:
        # LOAD THE PDF AND ADD THE PAGE FOR THE PRODUCT INFORMATION
        production_file = os.getenv('PRODUCTIONINFOFILE')
        pdf = FPDF()
        pdf.add_page()

        # ADD THE UNIQUE PRODUCT IDENTIFIERS TO THE PDF HEADER
        pdf.set_font('Arial', 'B', 30)
        pdf.multi_cell(190, 15, finished_product[os.getenv("UID")][0], 1, 'C')
        pdf.set_font('Arial', '', 20)
        pdf.multi_cell(190, 15, finished_product[os.getenv("DESC")][0], 1, 'C')
        lot = f"LOT:    {finished_product[os.getenv('LOT')][0]}"
        bbe = f"BBE:    {finished_product[os.getenv('BBE')][0]}"
        order_info = f"ORDER ID:     {str(finished_product[os.getenv('POID')][0])}        |          ORDER QTY:    {str(finished_product[os.getenv('POQ')][0])}"
        pdf.set_font('Arial', 'B', 15)
        pdf.multi_cell(190, 12, lot, 1, 'C')
        pdf.multi_cell(190, 12, bbe, 1, 'C')
        pdf.multi_cell(190, 12, order_info, 1, 'C')

        # ADD PRODUCT COMPONENTS TO THE PDF THE PDF
        if product_components != None:
            pdf.set_font('Arial', '', 11)
            for component in product_components:
                print_info = f"CODE:    {product_components[component][os.getenv('COMP1')]}     |  QTY: {product_components[component][os.getenv('COMP3')]} | {product_components[component][os.getenv('COMP2')]}"
                pdf.multi_cell(190, 15, print_info , 0, 'L')

        # OUTPUT THE DATA TO THE PDF FILE
        pdf.output(production_file, 'F')
        return(production_file)
    except Exception as ex:
        print("Data could not be processed: \n", ex)
