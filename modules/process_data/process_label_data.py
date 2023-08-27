import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv("../.env")

def process_label_data(data):
    try:

        label_data = data.loc[:, [ os.getenv('LABELINPUT1'), os.getenv('LABELINPUT2'), os.getenv('LABELINPUT3', os.getenv('LABELINPUT4')), os.getenv('LABELINPUT5'), os.getenv('LABELINPUT6'), os.getenv('LABELINPUT7'), os.getenv('LABELINPUT8')]]


        label_dataa = label_data[label_data[os.getenv('LABELINPUT8')].notna()]

        return(label_dataa)

    except Exception as ex:

        print("Data could not be processed: \n", ex)


