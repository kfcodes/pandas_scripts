import os
from dotenv import load_dotenv
load_dotenv("../../.env")
import pandas as pd
from .connect import database_connection

def get_production_info(selection):
    try:
        info = pd.read_sql(selection ,database_connection())
        values = info.to_dict(orient='list')
        return values
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

def get_database_info2(selection):
    try:
        info = pd.read_sql(selection ,database_connection())
        return(info);
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
