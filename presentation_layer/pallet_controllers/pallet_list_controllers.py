from data_access_layer.read_database_functions import read_selection_to_list

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

async def get_all_pallets():
    try:
        pallet = read_selection_to_list(f"{os.getenv('')}'{id}'")
        return pallet
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_pallet_group(id):
    try:
        pallets = read_selection_to_list(f"{os.getenv('')}'{id}'")
        return pallets
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_pallet_details(id):
    try:
        pallet = read_selection_to_list(f"{os.getenv('')}'{id}'")
        return pallet
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_possible_pallets():
    try:
        pallets = read_selection_to_list(f"{os.getenv('')}")
        return pallets
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_recent_pallets():
    try:
        pallets = read_selection_to_list(f"{os.getenv('')}")
        return pallets
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_pallet_data():
    try:
        pallets = read_selection_to_list(f"{os.getenv('')}")
        return pallets
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_latest_pallet_data():
    try:
        pallets = read_selection_to_list(f"{os.getenv('')}")
        return pallets
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_picklist():
    try:
        pallets = read_selection_to_list(f"{os.getenv('')}")
        return pallets
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_data():
    try:
        pallets = read_selection_to_list(f"{os.getenv('')}")
        return pallets
    except Exception as ex:
        print("Data could not be processed: \n", ex)
