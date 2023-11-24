from data_access_layer.read_database_functions import read_selection_to_list

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

async def create_pallet_item_with_id(id):
    try:
        pallet_item = read_selection_to_list(f"{os.getenv('')}'{id}'")
        return pallet_item
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_items_on_pallet(id):
    try:
        items = read_selection_to_list(f"{os.getenv('')}'{id}'")
        return items
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def update_pallet_item_by_id(id):
    try:
        item = read_selection_to_list(f"{os.getenv('')}'{id}'")
        return item
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def delete_pallet_item_by_id(id):
    try:
        items = read_selection_to_list(f"{os.getenv('')}'{id}'")
        return items
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_all_pallet_items(id):
    try:
        items = read_selection_to_list(f"{os.getenv('')}'{id}'")
        return items
    except Exception as ex:
        print("Data could not be processed: \n", ex)
