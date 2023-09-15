import os
from dotenv import load_dotenv
load_dotenv("../../.env")
import pandas as pd
from .connect import database_connection

def get_production_info(selection):
    try:
        info = pd.read_sql(selection ,database_connection())
        values = info.values.tolist()[0]
        id = values[2]
        description = values[3]
        lot = values[4]
        bbe = values[5]
        order_id = values[1]
        order_quantity = values[7]
        return_values = (id, description, lot, bbe, order_id, order_quantity);
        print(type(return_values));
        return return_values
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

def get_database_info2(selection):
    try:
        info = pd.read_sql(selection ,database_connection())
        return(info);
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
