import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv(".env")

def get_pl_data():
    product_database_dataframe = pd.ExcelFile(os.getenv('PL'))
    for sheet in product_database_dataframe.sheet_names:
        sheet_data = product_database_dataframe.parse(sheet, usecols="f:g,h")
        noNa = sheet_data.dropna(axis=0, how = 'all')
        print(noNa)
