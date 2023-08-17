import pandas as pd
import sqlalchemy as sqlalchemy
from sql import write_pandas_dataframe_to_sql
import os
from dotenv import load_dotenv
load_dotenv(".env")
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert, select

metadata = MetaData()


def get_packing_list_values(no_nan, value ):
    dispatch_date_row = no_nan[no_nan.isin([value]).any(axis=1)]
    dispatch_date_row_2 = dispatch_date_row.dropna(axis=1)
    dispatch_date_row_3 = dispatch_date_row_2.iloc[:,2]
    dispatch_date_row_4 =   dispatch_date_row_3.astype(str).str.lower()
    dispatch_date_row_5 = dispatch_date_row_4.values[0]
    dispatch_date_row_6 = dispatch_date_row_5.split(' ')
    dispatch_date_row_7 = dispatch_date_row_6[0]
    return dispatch_date_row_7

def get_height(row):
    the = row.loc['Dimensions']
    dimensions = the.split('x')
    return dimensions[2]

def get_lot(row):
    the = row.loc['Lot BBE']
    dimensions = the.split()
    return dimensions[0]

def get_bbe(row):
    the = row.loc['Lot BBE']
    dimensions = the.split()
    return dimensions[1]

def get_pallet_type(row):
    the = row.loc['Dimensions']
    dimensions = the.split('x')
    if dimensions[1] == '80':
        return 3
    else:
        return 1

def old_code(): 
    for root, directories, files in os.walk(path):
        for file in files:
            if(file.endswith(".xlsx") and file.startswith("the")):
                file_path = os.path.join(root, file)
                sheets = pd.ExcelFile(file_path)
                for sheet in sheets.sheet_names:
                        print(correct_column_names)

product_database_dataframe = pd.ExcelFile(os.getenv('PACKING_LIST'))

def lower_case(dataframe):
    dataframe[os.getenv('Column7')] = dataframe[os.getenv('Column7')].astype(str).str.lower()
    dataframe[os.getenv('Column8')] = dataframe[os.getenv('Column8')].astype(str).str.lower()
    dataframe[os.getenv('Column9')] = dataframe[os.getenv('Column9')].astype(str).str.lower()
    dataframe[os.getenv('Column10')] = dataframe[os.getenv('Column10')].astype(str).str.lower()

get_pallet_data()
get_pallet_products()
