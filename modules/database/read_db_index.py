import os
from dotenv import load_dotenv
load_dotenv("../../.env")
import pandas as pd
from .connect import database_connection

def get_production_documentation(selection):
    try:
        finished_product_info = pd.read_sql(selection ,database_connection())
        return(finished_product_info);
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

def get_product_components(id):
    try:
        selection = "COMPONENTS"
        components = read_select_to_dataframe(selection, id)
        return(components);
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
