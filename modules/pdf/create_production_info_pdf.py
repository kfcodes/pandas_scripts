from fpdf import FPDF
import os
from dotenv import load_dotenv
load_dotenv("../.env")

def create_production_info_pdf(finished_product, product_components):
    try:

        lot = f"LOT:    {finished_product[os.getenv('L')][0]}"
        bbe = f"BBE:    {finished_product[os.getenv('B')][0]}"
        p = f"ORDER ID:     {str(int(finished_product[os.getenv('P')][0]))}        |          ORDER QTY:    {str(int(finished_product[os.getenv('PQ')][0]))}"

        production_file = os.getenv('PRODUCTIONINFOFILE')

        pdf = FPDF()
        pdf.add_page()

        # ADD THE PRODUCT INFO TO THE PDF
        pdf.set_font('Arial', 'B', 40)
        pdf.multi_cell(190, 20, finished_product[os.getenv("UID")][0], 1, 'C')
        pdf.set_font('Arial', '', 20)
        pdf.multi_cell(190, 15, finished_product[os.getenv("DESC")][0], 1, 'C')


        # ADD THE IDENTIFIER DATA TO THE PDF
        pdf.set_font('Arial', 'B', 15)
        pdf.multi_cell(190, 15, lot, 1, 'C')
        pdf.multi_cell(190, 15, bbe, 1, 'C')
        pdf.multi_cell(190, 15, p, 1, 'C')


        print(product_components)

        pdf.output(production_file, 'F')

        print("done")

        # return(production_file)

    except Exception as ex:
        print("Data could not be processed: \n", ex)
