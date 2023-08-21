import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv("../.env")

def process_db_data(data):
    try:
        database_data = data.loc[:, [ os.getenv('DBINPUT1'), os.getenv('DBINPUT2'), os.getenv('DBINPUT3'), os.getenv('DBINPUT4')]]
        new_data = database_data.rename(columns={os.getenv('DBINPUT1'):os.getenv('DBOUTPUT1'),os.getenv('DBINPUT2'):os.getenv('DBOUTPUT2'),os.getenv('DBINPUT3'):os.getenv('DBOUTPUT3'),os.getenv('DBINPUT4'):os.getenv('DBOUTPUT4'),})
        return(new_data)
    except Exception as ex:
        print("Data could not be processed: \n", ex)


