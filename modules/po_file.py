from xlsx.read_database_file import read_xlsx_file
from process_data.process_po_data import process_data
from database.index import update_po

data= read_xlsx_file('PO_FILE')
formatted_data = process_data(data);
update_po(formatted_data);
