import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv("../.env")

def process_schedule_data(data):
    try:

        sheet_data_part_1 = data.loc[:, [ os.getenv('SCHEDULEINPUT1'), os.getenv('SCHEDULEINPUT2'), os.getenv('SCHEDULEINPUT3')]]

        sheet_data_part_2 = data.loc[:, [ os.getenv('SCHEDULEINPUT6'), os.getenv('SCHEDULEINPUT7'), os.getenv('SCHEDULEINPUT8')]]

        sheet_data_part_3 = data.loc[:, [ os.getenv('SCHEDULEINPUT11'), os.getenv('SCHEDULEINPUT12'), os.getenv('SCHEDULEINPUT13')]]
        
        sheet_data_part_4 = data.loc[:, [ os.getenv('SCHEDULEINPUT16'), os.getenv('SCHEDULEINPUT17'), os.getenv('SCHEDULEINPUT18')]]


        processed_data = sheet_data.rename(columns={os.getenv('SCHEDULEINPUT1'):os.getenv('SCHEDULEOUTPUT1'),os.getenv('SCHEDULEINPUT2'):os.getenv('SCHEDULEOUTPUT2'),os.getenv('SCHEDULEINPUT3'):os.getenv('SCHEDULEOUTPUT3'),os.getenv('SCHEDULEINPUT4'):os.getenv('SCHEDULEOUTPUT4'),})

        return(processed_data)

    except Exception as ex:

        print("Data could not be processed: \n", ex)


