from database.read_db_index import get_production_documentation

# Get the info from the DB
get_production_documentation(id);
# Create the PDF file
pdf = create_pdf_file(data);
# Print the PDF file
print_pdf(pdf);
