import os
from dotenv import load_dotenv
load_dotenv("../../.env")
import pandas as pd
from .connect import database_connection

def get_database_info(selection):
    try:
        info = pd.read_sql(selection ,database_connection())
        return(info);
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
