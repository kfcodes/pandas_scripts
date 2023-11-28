from business_logic_layer.xlsx_logic_module.read_xlsx_file import read_data_in_sheet
from business_logic_layer.pandas_logic_module.process_label_data import process_label_data
from data_access_layer.write_database_functions import update_labels

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

def process_label_file():
    try:
        data = read_data_in_sheet('LABELSFILE', os.getenv('SHEETNAME'))
        processed_data = process_label_data(data);
        update_labels(processed_data);

    except Exception as ex:
        print("Data could not be processed: \n", ex)
