from business_logic_layer.external_module_controllers.excel_file_logic.read_xlsx_file import read_data_in_sheet
from business_logic_layer.external_module_controllers.data_analysis_logic.process_label_data import process_label_data, process_label_data_2, process_label_data_3 
from physical_layer.data_access_layer.write_database_functions import update_labels

import os
from dotenv import load_dotenv
load_dotenv("../../.server_config_files/fastAPI.env")

def process_label_file():
    try:
        data = read_data_in_sheet('LABELSFILE', os.getenv('SHEETNAME'))
        processed_data = process_label_data(data);
        data_2 = read_data_in_sheet('LABELSFILE', os.getenv('SHEETNAME_2'))
        processed_data_2 = process_label_data_2(data_2);
        # data_3 = read_data_in_sheet('LABELSFILE', os.getenv('SHEETNAME_3'))
        # processed_data_3 = process_label_data_3(data_3);
        # update_labels(processed_data, processed_data_2, processed_data_3);
        update_labels(processed_data, processed_data_2);

    except Exception as ex:
        print("Data could not be processed: \n", ex)
