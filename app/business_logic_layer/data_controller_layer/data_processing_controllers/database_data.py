from business_logic_layer.external_module_controllers.excel_file_logic.read_xlsx_file import read_data
from business_logic_layer.external_module_controllers.data_analysis_logic.process_database_data import process_db_data
from physical_layer.data_access_layer.write_database_functions import update_db

def process_db_file():
    try:
        data= read_data('DBFILE')
        processed_data = process_db_data(data);
        update_db(processed_data);

    except Exception as ex:
        print("Data could not be processed: \n", ex)
