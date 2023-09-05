from fpdf import FPDF
import os
from dotenv import load_dotenv
load_dotenv("../.env")

def create_pdf():
    try:
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font('Arial', 'B', 16)
        pdf.cell(40, 10, 'Hello World!')

        pdf.output('test.pdf', 'F')
        return('test.pdf')
    except Exception as ex:
        print("Data could not be processed: \n", ex)
