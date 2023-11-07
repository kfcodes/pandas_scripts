from business_logic_layer.xlsx_controllers.read_xlsx_file import read_data
from business_logic_layer.pandas_controllers.process_database_data import process_db_data
from data_access_layer.write_database_functions import update_db

def process_db_file():

    try:
        data= read_data('DBFILE')
        processed_data = process_db_data(data);
        # print(processed_data)
        update_db(processed_data);

    except Exception as ex:
        print("Data could not be processed: \n", ex)
