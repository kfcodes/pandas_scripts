from ..xlsx_controllers.read_xlsx_file import read_data_after_first_row
from ..pandas_data_analysis_controllers.process_schedule_data import process_schedule_data
from ..database_controllers.write_db_index import update_schedule

import os
from dotenv import load_dotenv
load_dotenv("../../../.env")

def process_schedule_file(sheet):
    
    try:

        data= read_data_after_first_row('SCHEDULEFILE', sheet)
        processed_data = process_schedule_data(data);
        update_schedule(processed_data);
         
    except Exception as ex:
        print("Data could not be processed: \n", ex)
