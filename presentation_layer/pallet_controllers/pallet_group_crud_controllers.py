from data_access_layer.read_database_functions import read_selection_to_list, read_to_list_index
from data_access_layer.write_database_functions import db

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

async def create_new_pallet_list():
    try:
        db(f"{os.getenv('CREATENEWPALLETLIST')}")
        pallet_list_info = read_selection_to_list(f"{os.getenv('GETNEWESTPALLETLIST')}")
        return pallet_list_info
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_pallet_list_info(id):
    try:
        pallet_list = read_to_list_index(f"{os.getenv('GETPALLET_LIST')}'{int(id)}'")
        return pallet_list
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def update_pallet_list(id, new_pallet_list_data):
    try:
        new_pallet_list_data = str(new_pallet_list_data).replace(' ', ' ,').replace('None', 'Null')
        update_string = str(os.getenv('UPDATEPALLETLIST'))
        updated_pallet_list_info = db(update_string.format(new_pallet_list_data,id))
        return updated_pallet_list_info
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def delete_pallet_list(id):
    try:
        pallet_list = db(f"{os.getenv('DELETEPALLETLIST')}{id}")
        return pallet_list
    except Exception as ex:
        print("Data could not be processed: \n", ex)
