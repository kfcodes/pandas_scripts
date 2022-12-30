# Added function to convert all data to lowercase
import pandas as pd
import sqlalchemy as sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import mysql.connector
import db_connection
import os
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from dotenv import load_dotenv
load_dotenv(".env")

engine = db_connection.create_connection()

products = pd.read_sql(os.getenv('pdb_table'), engine, columns=[os.getenv('Column_1'), os.getenv('Column_2')])

brands = pd.read_sql(os.getenv('b_table'), engine, columns = [os.getenv('Column_6')], index_col=os.getenv('Column_5'))

product_options = products[os.getenv('Column_1')].tolist()

production_schedules = pd.ExcelFile(os.getenv('PRODUCTION_SCHEDULES'))
print(production_schedules)

def lower_case(dataframe):
    dataframe[os.getenv('Column7')] = dataframe[os.getenv('Column7')].astype(str).str.lower()
    dataframe[os.getenv('Column8')] = dataframe[os.getenv('Column8')].astype(str).str.lower()
    dataframe[os.getenv('Column9')] = dataframe[os.getenv('Column9')].astype(str).str.lower()
    dataframe[os.getenv('Column10')] = dataframe[os.getenv('Column10')].astype(str).str.lower()
