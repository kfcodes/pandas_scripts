from fpdf import FPDF
import os
from dotenv import load_dotenv
load_dotenv("../.env")

def create_production_info_pdf(finished_product, product_components):
    try:
        production_file=os.getenv('PRODUCTIONINFOFILE')
        pdf = FPDF()
        pdf.add_page()

        # Print the UID on the PDF
        pdf.set_font('Arial', 'B', 40)
        # Centered text in a framed 20*10 mm cell and line break
        pdf.multi_cell(190, 20, finished_product[os.getenv("UID")][0], 1, 'C')

        # Print the Production information
        pdf.set_font('Arial', '', 20)
        pdf.multi_cell(190, 15, finished_product[os.getenv("DESC")][0], 1, 'C')

        pdf.output(production_file, 'F')

        print("done")

        # return(production_file)

    except Exception as ex:
        print("Data could not be processed: \n", ex)
