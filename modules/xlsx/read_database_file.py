import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv("../.env")

def read_xlsx_file(file):
    try:
        df = pd.read_excel(os.getenv(file))
        return(df)
    except Exception as ex:
        print("Could not read the file: \n", ex)
