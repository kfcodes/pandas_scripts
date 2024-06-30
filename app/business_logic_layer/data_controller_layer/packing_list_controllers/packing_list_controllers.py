from physical_layer.data_access_layer.read_database_functions import read_selection_to_list, read_to_list_index
from physical_layer.data_access_layer.write_database_functions import db, db2

import os
from dotenv import load_dotenv
load_dotenv(".env")

async def get_open_packing_lists():
    try:
        packing_lists = read_selection_to_list(f"{os.getenv('OPENPACKINGLISTS')}")
        return packing_lists;
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_open_packing_list_names():
    try:
        packing_list_names = read_selection_to_list(f"{os.getenv('OPENPACKINGLISTNAMES')}")
        return packing_list_names;
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_pallets_not_on_a_packing_list():
    try:
        pallets = read_selection_to_list(f"{os.getenv('PALLETSNOTONPACKINGLIST')}")
        return pallets;
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_packing_list_pallets(id):
    try:
        packing_list_pallets = read_selection_to_list(f"{os.getenv('PACKINGLISTPALLETS')}{int(id)}")
        return packing_list_pallets;
    except Exception as ex:
        print("Data could not be processed: \n", ex)
