from fpdf import FPDF
import os
from dotenv import load_dotenv
load_dotenv("../.env")

def create_production_info_pdf(data):
    try:

        production_file=os.getenv('PRODUCTIONINFO')

        pdf = FPDF()
        pdf.add_page()

        pdf.set_font('Arial', 'B', 16)
        pdf.cell(40, 10, 'Hello World!2')

        pdf.output(production_file, 'F')

        return(production_file)

    except Exception as ex:
        print("Data could not be processed: \n", ex)
