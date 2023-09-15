from fpdf import FPDF
import os
from dotenv import load_dotenv
load_dotenv("../.env")

def create_production_info_pdf(finished_product, product_components):
    try:
        production_file=os.getenv('PRODUCTIONINFOFILE')

        pdf = FPDF()
        pdf.add_page()

        pdf.set_font('Arial', 'B', 16)
        # pdf.cell(40, 10, finished_product)
        pdf.cell(40, 10, "test")

        pdf.set_font('Arial', 'B', 16)
        # pdf.cell(40, 10, product_components)
        pdf.cell(40, 10, "test")
        pdf.cell(40, 10, "test")
        pdf.cell(40, 10, "test")
        pdf.cell(40, 10, "test")

        pdf.output(production_file, 'F')

        print("done")

        # return(production_file)

    except Exception as ex:
        print("Data could not be processed: \n", ex)
