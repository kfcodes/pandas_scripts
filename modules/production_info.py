from database.read_db_index import get_production_documentation
from pdf.create_pdf import create_pdf
from print.print_pdf import print_a4_pdf

def print_production_pdf(id):
    try:

        data = get_production_documentation(id);

        pdf_file = create_pdf(data);

        print_a4_pdf(pdf_file)

    except Exception as ex:
        print("Could not print the PDF file due to the following: \n", ex)
