from physical_layer.data_access_layer.read_database_functions import read_to_list_index
from physical_layer.data_access_layer.write_database_functions import db
import math

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

async def create_pallet_item_with_id(pallet_id):
    try:
        new_pallet_item_string = str(f"{os.getenv('CREATENEWPALLETITEM')}")
        new_pallet_item = db(new_pallet_item_string.format(int(pallet_id)))
        return new_pallet_item
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_item_on_pallet(item_id):
    try:
        item = read_to_list_index(f"{os.getenv('GETPALLETITEM')}{int(item_id)}")
        item = item[0]
        print(item)
        return item;
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def update_pallet_item(item_id, new_item_data):
    try:
        new_item_data = str(new_item_data).replace(' ', ' ,').replace('None', 'Null')
        update_string = str(os.getenv('UPDATEPALLETITEM'))
        updated_item = db(update_string.format(new_item_data, item_id))
        return updated_item
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def delete_pallet_item(item_id):
    try:
        items = db(f"{os.getenv('DELETEPALLETITEM')}'{int(item_id)}'")
        print(items)
        return f"Pallet item with id of {int(item_id)} has been deleted"
    except Exception as ex:
        print("Data could not be processed: \n", ex)
