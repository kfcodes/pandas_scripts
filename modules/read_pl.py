import pandas as pd
import sqlalchemy as sqlalchemy
from sql import write_pandas_dataframe_to_sql
import os
from dotenv import load_dotenv
load_dotenv(".env")
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert, select

metadata = MetaData()

product_database_dataframe = pd.ExcelFile(os.getenv('PACKING_LIST'))

def get_pallet_data():
    for sheet in product_database_dataframe.sheet_names:
        sheet_data = product_database_dataframe.parse(sheet, usecols="f:g,h")
        noNa = sheet_data.dropna(axis=0, how = 'all')
        print("this is the pallet data")
        print(noNa)
