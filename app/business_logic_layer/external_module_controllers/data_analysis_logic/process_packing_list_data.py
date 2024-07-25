import pandas as pd

import os
from dotenv import load_dotenv
load_dotenv("../.env")

def process_data(data):

    try:
        df = pd.json_normalize(data)
        return(df)

    except Exception as ex:
        print("Data could not be processed: \n", ex)

