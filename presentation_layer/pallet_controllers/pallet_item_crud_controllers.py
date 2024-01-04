from data_access_layer.read_database_functions import read_selection_to_list, read_to_list_index
from data_access_layer.write_database_functions import db
import math

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

async def create_pallet_item_with_id(pallet_id):
    try:
        new_pallet_item = db(f"{os.getenv('CREATEPALLETITEM')}({int(pallet_id)})")
        return new_pallet_item
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_items_on_pallet(pallet_id):
    try:
        pallet_items = [];
        items = read_to_list_index(f"{os.getenv('GETPALLETITEMS')}{int(pallet_id)}")
        for key, val in items.items():
            if math.isnan(val["quantity"]):
                val["quantity"] = 0;
            else:
                val["quantity"] = int(val["quantity"]);
            pallet_items.append(val)
        return pallet_items;
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
        items = db(f"{os.getenv('DELETEPALLETITEM')}'{int(item_id)}'")
        return items
    except Exception as ex:
        print("Data could not be processed: \n", ex)

# PALLET ITEMS LIST FUNCTIONS
async def get_new_pallet_items():
    try:
        resultlist = [];
        pallet_items = read_to_list_index(f"{os.getenv('GETNEWPALLETITEMS')}")
        for key, val in pallet_items.items():
            resultlist.append(val)
        return resultlist;
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_all_pallet_items():
    try:
        resultlist = [];
        pallet_items = read_to_list_index(f"{os.getenv('GETALLPALLETITEMS')}")
        for key, val in pallet_items.items():
            resultlist.append(val)
        return resultlist;
    except Exception as ex:
        print("Data could not be processed: \n", ex)

