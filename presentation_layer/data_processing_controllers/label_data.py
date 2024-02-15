from business_logic_layer.xlsx_logic_module.read_xlsx_file import read_data_in_sheet
from business_logic_layer.pandas_logic_module.process_label_data import process_label_data, process_label_data_2
from data_access_layer.write_database_functions import update_labels

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

def process_label_file():
    try:
        data = read_data_in_sheet('LABELSFILE', os.getenv('SHEETNAME'))
        processed_data = process_label_data(data);
        data_2 = read_data_in_sheet('LABELSFILE', os.getenv('SHEETNAME_2'))
        processed_data_2 = process_label_data_2(data_2);
        update_labels(processed_data, processed_data_2);

    except Exception as ex:
        print("Data could not be processed: \n", ex)
