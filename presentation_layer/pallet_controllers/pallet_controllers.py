from data_access_layer.read_database_functions import read_selection_to_list

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

async def create_pallet():
    try:
        pallet_id = read_selection_to_list(f"{os.getenv('')}")
        return pallet_id
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_pallet_by_id(id):
    try:
        pallet = read_selection_to_list(f"{os.getenv('')}'{id}'")
        return pallet
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def update_pallet_by_id(id):
    try:
        pallet = read_selection_to_list(f"{os.getenv('')}'{id}'")
        return pallet
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def delete_pallet_by_id(id):
    try:
        pallet = read_selection_to_list(f"{os.getenv('')}'{id}'")
        return pallet
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def combine_pallets():
    try:
        pallets = read_selection_to_list(f"{os.getenv('')}'{id}'")
        return pallets
    except Exception as ex:
        print("Data could not be processed: \n", ex)

