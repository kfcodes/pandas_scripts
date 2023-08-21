import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv("../.env")

def process_component_data(data):
    try:

        component_data = data.loc[:, [ os.getenv('COMPONENTINPUT1'), os.getenv('COMPONENTINPUT2'), os.getenv('COMPONENTINPUT3')]]

        processed_data = component_data.rename(columns={os.getenv('COMPONENTINPUT1'):os.getenv('COMPONENTOUTPUT1'),os.getenv('COMPONENTINPUT2'):os.getenv('COMPONENTOUTPUT2'),os.getenv('COMPONENTINPUT3'):os.getenv('COMPONENTOUTPUT3'),})

        return(processed_data)

    except Exception as ex:

        print("Data could not be processed: \n", ex)


