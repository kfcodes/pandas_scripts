from data_access_layer.read_database_functions import read_selection_to_list
from data_access_layer.write_database_functions import db

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

async def create_pallet_item_with_id(pallet_id):
    try:
        new_pallet_item = db(f"{os.getenv('CREATEPALLETITEM')}({pallet_id})")
        return new_pallet_item
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_items_on_pallet(pallet_id):
    try:
        pallet_items = read_selection_to_list(f"{os.getenv('GETPALLETITEMS')}'{pallet_id}'")
        return pallet_items
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def update_pallet_item(item_id):
    try:
        updated_item = db(f"{os.getenv('UPDATEPALLETITEM')}'{item_id}'")
        return updated_item
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def delete_pallet_item(item_id):
    try:
        items = db(f"{os.getenv('DELETEPALLETITEM')}'{item_id}'")
        return items
    except Exception as ex:
        print("Data could not be processed: \n", ex)
