import sys
from database.read_db_index import get_production_documentation, get_product_components
from pdf.create_production_info_pdf import create_production_info_pdf
from print.print_pdf import print_a4_pdf

id = str(sys.argv[1])
info = get_production_documentation(id);
components = get_product_components(id);
pdf_file = create_production_info_pdf(info,components);
# print_a4_pdf(pdf_file)
