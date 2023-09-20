import pprint
from fpdf import FPDF
import os
from dotenv import load_dotenv
load_dotenv("../.env")

def create_production_info_pdf(finished_product, product_components):
    try:
        production_file = os.getenv('PRODUCTIONINFOFILE')

        pdf = FPDF()
        pdf.add_page()

        # ADD THE UNIQUE PRODUCT IDENTIFIERS TO THE PDF
        pdf.set_font('Arial', 'B', 40)
        pdf.multi_cell(190, 20, finished_product[os.getenv("UID")][0], 1, 'C')

        pdf.set_font('Arial', '', 20)
        pdf.multi_cell(190, 15, finished_product[os.getenv("DESC")][0], 1, 'C')
        lot = f"LOT:    {finished_product[os.getenv('L')][0]}"
        bbe = f"BBE:    {finished_product[os.getenv('B')][0]}"
        order_info = f"ORDER ID:     {str(int(finished_product[os.getenv('P')][0]))}        |          ORDER QTY:    {str(int(finished_product[os.getenv('PQ')][0]))}"
        pdf.set_font('Arial', 'B', 15)
        pdf.multi_cell(190, 15, lot, 1, 'C')
        pdf.multi_cell(190, 15, bbe, 1, 'C')
        pdf.multi_cell(190, 15, order_info, 1, 'C')

        # ADD PRODUCT COMPONENTS TO THE PDF
        pdf.set_font('Arial', '', 11)
        for component in product_components:
            print_info = f" {product_components[component][os.getenv('COMP1')]}  |   {product_components[component][os.getenv('COMP2')]}  |  QTY: {product_components[component][os.getenv('COMP3')]}"
            pdf.multi_cell(190, 20, print_info , 1, 'C')

        pdf.output(production_file, 'F')

        print("done")

        return(production_file)

    except Exception as ex:
        print("Data could not be processed: \n", ex)
