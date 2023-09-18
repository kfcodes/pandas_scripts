from xlsx.read_xlsx_file import read_full_xlsx_file , read_xlsx_file_skip_first_row
from process_data.process_po_data import process_po_data
from database.write_db_index import update_po, update_poi

def process_po_files():
    try:
        inputdata = read_xlsx_file_skip_first_row('POFILE')
        po_name_data = read_full_xlsx_file('PONAMEFILE')
        data = process_po_data(inputdata, po_name_data);
        update_po(data[0]);
        update_poi(data[1]);
    except Exception as ex:
        print("Data could not be processed: \n", ex)

process_po_files()
