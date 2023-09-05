import os
from dotenv import load_dotenv
load_dotenv("../../.env")
import pandas as pd
from .connect import database_connection

def read_to_dataframe(name):
    try:

        data = pd.read_sql(os.getenv(name),database_connection())
        return(data)

    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

def read_select_to_dataframe(SELECTION, id):
    try:

        selection = os.getenv(SELECTION)+id

        data = pd.read_sql(selection ,database_connection())

        return(data)

    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
