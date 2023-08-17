import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv("../.env")

def process_data(data):
    try:
        database_data = data.loc[:, [ os.getenv('Column1'), os.getenv('Column2'), os.getenv('Column3'), os.getenv('Column4')]]
        new_data = database_data.rename(columns={os.getenv('Column1'):os.getenv('Column_1'),os.getenv('Column2'):os.getenv('Column_2'),os.getenv('Column3'):os.getenv('Column_3'),os.getenv('Column4'):os.getenv('Column_4'),})
        return(new_data)
    except Exception as ex:
        print("Data could not be processed: \n", ex)


