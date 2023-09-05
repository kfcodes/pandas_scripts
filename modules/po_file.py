from xlsx.read_database_file import read_xlsx_file
from xlsx.read_database_file import read_xlsx_file_remove_first_row
from process_data.process_po_data import process_po_data
from database.write_db_index import update_po, update_poi

inputdata = read_xlsx_file_remove_first_row('POFILE')
po_name_data = read_xlsx_file('PONAMEFILE')
data = process_po_data(inputdata, po_name_data);
update_po(data[0]);
update_poi(data[1]);
