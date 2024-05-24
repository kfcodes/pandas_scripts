from data_access_layer.read_database_functions import read_selection_to_list
import os
from dotenv import load_dotenv
load_dotenv("../.env")

async def get_current_production():
    try:
        production = read_selection_to_list(f"{os.getenv('')}")
        return production
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_all_production(id):
    try:
        production = read_selection_to_list(f"{os.getenv('')}'{id}'")
        return production
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_production_records_by_id(id):
    try:
        production = read_selection_to_list(f"{os.getenv('')}'{id}'")
        return production
    except Exception as ex:
        print("Data could not be processed: \n", ex)
