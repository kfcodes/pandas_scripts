import os
from dotenv import load_dotenv
load_dotenv("../../.env")
import pandas as pd
from connect import database_connection

def getData(name):
    try:
        sql_data = pd.read_sql(os.getenv(name),database_connection())
        return(sql_data)
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
