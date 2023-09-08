import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv("../.env")

def process_schedule_data(data):
    try:

        # READ IN THE DATA
        sheet_data_part_1 = data.loc[:, [ os.getenv('SCHEDULEINPUT1'), os.getenv('SCHEDULEINPUT2'), os.getenv('SCHEDULEINPUT3')]]
        sheet_data_part_2 = data.loc[:, [ os.getenv('SCHEDULEINPUT6'), os.getenv('SCHEDULEINPUT7'), os.getenv('SCHEDULEINPUT8')]]
        sheet_data_part_3 = data.loc[:, [ os.getenv('SCHEDULEINPUT11'), os.getenv('SCHEDULEINPUT12'), os.getenv('SCHEDULEINPUT13')]]
        sheet_data_part_4 = data.loc[:, [ os.getenv('SCHEDULEINPUT16'), os.getenv('SCHEDULEINPUT17'), os.getenv('SCHEDULEINPUT18')]]

        # RENAME THE COLUMNS 
        renamed_data_part_1 = sheet_data_part_1.rename(columns={os.getenv('SCHEDULEINPUT1'):os.getenv('SCHEDULEOUTPUT1'),os.getenv('SCHEDULEINPUT2'):os.getenv('SCHEDULEOUTPUT2'),os.getenv('SCHEDULEINPUT3'):os.getenv('SCHEDULEOUTPUT3'),})
        renamed_data_part_2 = sheet_data_part_2.rename(columns={os.getenv('SCHEDULEINPUT6'):os.getenv('SCHEDULEOUTPUT6'),os.getenv('SCHEDULEINPUT7'):os.getenv('SCHEDULEOUTPUT7'),os.getenv('SCHEDULEINPUT8'):os.getenv('SCHEDULEOUTPUT8'),})
        renamed_data_part_3 = sheet_data_part_3.rename(columns={os.getenv('SCHEDULEINPUT11'):os.getenv('SCHEDULEOUTPUT11'),os.getenv('SCHEDULEINPUT12'):os.getenv('SCHEDULEOUTPUT12'),os.getenv('SCHEDULEINPUT13'):os.getenv('SCHEDULEOUTPUT13'),})
        renamed_data_part_4 = sheet_data_part_4.rename(columns={os.getenv('SCHEDULEINPUT16'):os.getenv('SCHEDULEOUTPUT16'),os.getenv('SCHEDULEINPUT17'):os.getenv('SCHEDULEOUTPUT17'),os.getenv('SCHEDULEINPUT18'):os.getenv('SCHEDULEOUTPUT18'),})

        vertical_concat = pd.concat([renamed_data_part_1, renamed_data_part_2, renamed_data_part_3, renamed_data_part_4,], axis=0)

        vertical_concat.dropna();


        print(vertical_concat)




    except Exception as ex:

        print("Data could not be processed: \n", ex)


