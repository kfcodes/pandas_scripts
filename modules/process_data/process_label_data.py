import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv("../.env")

def process_label_data(data):
    try:

        label_data = data.loc[:, [ os.getenv('LABELINPUT1'), os.getenv('LABELINPUT2'), os.getenv('LABELINPUT3', os.getenv('LABELINPUT4')), os.getenv('LABELINPUT5'), os.getenv('LABELINPUT6'), os.getenv('LABELINPUT7')]]

        processed_data = label_data.rename(columns={os.getenv('LABELINPUT1'):os.getenv('LABELOUTPUT1'),os.getenv('LABELINPUT2'):os.getenv('LABELOUTPUT2'),os.getenv('LABELINPUT3'):os.getenv('LABELOUTPUT3'),os.getenv('LABELINPUT4'):os.getenv('LABELOUTPUT4'),os.getenv('LABELINPUT5'):os.getenv('LABELOUTPUT5'),os.getenv('LABELINPUT6'):os.getenv('LABELOUTPUT6'),os.getenv('LABELINPUT7'):os.getenv('LABELOUTPUT7'),})

        return(processed_data)

    except Exception as ex:

        print("Data could not be processed: \n", ex)


