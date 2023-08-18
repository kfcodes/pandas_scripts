from xlsx.read_database_file import read_xlsx_file
from process_data.process_po_data import process_data
from database.index import update_po, update_poi

inputdata= read_xlsx_file('PO_FILE')
data = process_data(inputdata);
update_po(data[0]);
update_poi(data[1]);
