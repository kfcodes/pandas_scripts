from business_logic_layer.external_module_controllers.excel_file_logic.read_xlsx_file import read_data
from business_logic_layer.external_module_controllers.data_analysis_logic.process_stock_data import process_stock_data
from physical_layer.data_access_layer.write_database_functions import update_stock

def process_stock_file():
    try:
        data = read_data('STOCKFILE')
        processed_data = process_stock_data(data);
        update_stock(processed_data);

    except Exception as ex:
        print("Data could not be processed: \n", ex)

