from business_logic_layer.xlsx_logic_module.read_xlsx_file import read_data
from business_logic_layer.pandas_logic_module.process_stock_data import process_stock_data
from data_access_layer.write_database_functions import update_stock

def process_stock_file():
    try:
        data = read_data('STOCKFILE')
        processed_data = process_stock_data(data);
        update_stock(processed_data);

    except Exception as ex:
        print("Data could not be processed: \n", ex)

