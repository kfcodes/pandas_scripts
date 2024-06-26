from business_logic_layer.external_module_controllers.excel_file_logic.read_xlsx_file import read_data, read_data_after_first_row
from business_logic_layer.external_module_controllers.data_analysis_logic.process_po_data import process_po_data
from physical_layer.data_access_layer.write_database_functions import update_po, update_poi

def process_po_files():
    try:
        inputdata = read_data_after_first_row('POFILE')
        po_name_data = read_data('PONAMEFILE')
        data = process_po_data(inputdata, po_name_data);
        update_po(data[0]);
        update_poi(data[1]);

    except Exception as ex:
        print("Data could not be processed: \n", ex)
