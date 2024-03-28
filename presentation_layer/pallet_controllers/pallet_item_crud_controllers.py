from data_access_layer.read_database_functions import read_to_list_index
from data_access_layer.write_database_functions import db
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

async def get_items_on_pallet(pallet_id):
    try:
        pallet_items = [];
        items = read_to_list_index(f"{os.getenv('GETPALLETITEMS')}{int(pallet_id)}")
        for key, val in items.items():
            if val["quantity"] is None or math.isnan(val["quantity"]):
                val["quantity"] = None;
            else:
                val["quantity"] = int(val["quantity"]);
            pallet_items.append(val)
        return pallet_items;
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
        return items
    except Exception as ex:
        print("Data could not be processed: \n", ex)
