from xlsx.read_database_file import read_xlsx_file
from process_data.process_po_data import process_po_data
from database.index import update_po, update_poi

# inputdata = read_xlsx_file('POFILE')
po_name_data = read_xlsx_file('PONAMEFILE')
# process_po_data(inputdata, po_name_data);
process_po_data(po_name_data);
# data = process_po_data(inputdata, po_name_data);
# update_po(data[0]);
# update_poi(data[1]);
