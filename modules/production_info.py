from database.read_db_index import get_production_documentation
from pdf.create_pdf import create_pdf
from print.print_pdf import print_pdf


def print_production_pdf(id):
    try:

        # Get the info from the DB
        data = get_production_documentation(id);
        # Create the PDF file
        pdf = create_pdf(data);
        # Print the PDF file
        print_pdf(pdf);

    except Exception as ex:
        print("Could not print the PDF file due to the following: \n", ex)
