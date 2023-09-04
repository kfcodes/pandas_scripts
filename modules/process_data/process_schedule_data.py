import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv("../.env")

def process_schedule_data(data):
    try:

        sheet_data = data.loc[:, [ os.getenv('SCHEDULEINPUT1'), os.getenv('SCHEDULEINPUT2'), os.getenv('SCHEDULEINPUT3'), os.getenv('SCHEDULEINPUT4')]]

        processed_data = sheet_data.rename(columns={os.getenv('SCHEDULEINPUT1'):os.getenv('SCHEDULEOUTPUT1'),os.getenv('SCHEDULEINPUT2'):os.getenv('SCHEDULEOUTPUT2'),os.getenv('SCHEDULEINPUT3'):os.getenv('SCHEDULEOUTPUT3'),os.getenv('SCHEDULEINPUT4'):os.getenv('SCHEDULEOUTPUT4'),})

        return(processed_data)

    except Exception as ex:

        print("Data could not be processed: \n", ex)


