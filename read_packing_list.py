import pandas as pd
import sqlalchemy as sqlalchemy
from sql import write_pandas_dataframe_to_sql
import os
from dotenv import load_dotenv
load_dotenv(".env")
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert, select

metadata = MetaData()

product_database_dataframe = pd.ExcelFile(os.getenv('PACKING_LIST'))

