import pandas as pd

import os
from dotenv import load_dotenv
load_dotenv("../.env")

def read_data(file):
    try:
        df = pd.read_excel(os.getenv(file))
        return(df)
    except Exception as ex:
        print("Could not read the file: \n", ex)

def read_data_after_first_row(file):
    try:
        df = pd.read_excel(os.getenv(file), skiprows=1)
        return(df)
    except Exception as ex:
        print("Could not read the file: \n", ex)

def read_data_in_sheet(file, sheet):
    try:
        df = pd.read_excel(os.getenv(file), sheet_name=sheet)
        return(df)
    except Exception as ex:
        print("Could not read the file: \n", ex)

def data_from_columns(file, columns):
    try:
        df = pd.read_excel(os.getenv(file), usecols=columns)
        return(df)
    except Exception as ex:
        print("Could not read the file: \n", ex)

def data_from_columns_in_sheet(file, sheet):
    try:
        df = pd.read_excel(os.getenv(file), skiprows=1, sheet_name=sheet )
        return(df)
    except Exception as ex:
        print("Could not read the file: \n", ex)
