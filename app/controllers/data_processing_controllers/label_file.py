from ..xlsx_controllers.read_xlsx_file import read_data_in_sheet
from ..pandas_data_analysis_controllers.process_label_data import process_label_data
from ..database_controllers.write_db_index import update_labels

import os
from dotenv import load_dotenv
load_dotenv("../../../.env")

def process_label_file():

    try:

        data = read_data_in_sheet('LABELSFILE', os.getenv('SHEETNAME'))
        processed_data = process_label_data(data);

        update_labels(processed_data);

    except Exception as ex:
        print("Data could not be processed: \n", ex)
