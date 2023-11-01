from ..xlsx_controllers.read_xlsx_file import read_data
from ..pandas_data_analysis_controllers.process_stock_data import process_stock_data
from ..database_controllers.write_db_index import update_stock

import os
from dotenv import load_dotenv
load_dotenv("../../../.env")

def process_stock_file():

    try:

        data = read_data('STOCKFILE')
        processed_data = process_stock_data(data);

        update_stock(processed_data);

    except Exception as ex:
        print("Data could not be processed: \n", ex)

