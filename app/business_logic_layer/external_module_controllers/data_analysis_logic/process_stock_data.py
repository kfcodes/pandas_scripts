import os
from dotenv import load_dotenv
load_dotenv("../.env")

def process_stock_data(data):

    try:

        database_data = data.loc[:, [ os.getenv('STOCKINPUT1'), os.getenv('STOCKINPUT2'), os.getenv('STOCKINPUT3'), os.getenv('STOCKINPUT4')]]

        processed_data = database_data.rename(columns={os.getenv('STOCKINPUT1'):os.getenv('STOCKOUTPUT1'),os.getenv('STOCKINPUT2'):os.getenv('STOCKOUTPUT2'),os.getenv('STOCKINPUT3'):os.getenv('STOCKOUTPUT3'),os.getenv('STOCKINPUT4'):os.getenv('STOCKOUTPUT4'),})

        return(processed_data)

    except Exception as ex:
        print("Data could not be processed: \n", ex)
