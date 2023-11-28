import pandas as pd
import os
from data_access_layer.database_connection import database_connection

def read_to_dataframe(name):
    try:
        data = pd.read_sql(os.getenv(name),database_connection())
        return(data)
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

def read_selected_data_to_dataframe(selected_data):
    try:
        data = pd.read_sql(selected_data ,database_connection())
        return(data)
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

def get_production_info(selection):
    try:
        info = pd.read_sql(selection ,database_connection())
        values = info.to_dict(orient='list')
        return values
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

def read_selection_to_list(selection):
    try:
        info = pd.read_sql(selection ,database_connection())
        values = info.to_dict(orient='list')
        return values
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

def read_to_list_index(selection):
    try:
        info = pd.read_sql(selection ,database_connection())
        values = info.to_dict(orient='index')
        return values
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

def get_production_components(selection):
    try:
        info = pd.read_sql(selection ,database_connection())
        values = info.to_dict(orient='index')
        return values
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

def get_label_data(selection):
    try:
        info = pd.read_sql(selection ,database_connection())
        values = info.to_dict(orient='index')
        return values
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
