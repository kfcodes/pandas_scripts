from data_access_layer.read_database_functions import read_selection_to_list, read_to_list_index
from data_access_layer.write_database_functions import db

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

async def create_new_pallet_group():
    try:
        db(f"{os.getenv('CREATENEWPALLETGROUP')}")
        pallet_group_info = read_selection_to_list(f"{os.getenv('GETNEWESTPALLETGROUP')}")
        return pallet_group_info
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_pallet_group_info(id):
    try:
        pallet_group = read_to_list_index(f"{os.getenv('GETPALLETGROUPINFO')}'{int(id)}'")
        return pallet_group
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def update_pallet_group(id, new_pallet_group_data):
    try:
        new_pallet_group_data = str(new_pallet_group_data).replace(' ', ' ,').replace('None', 'Null')
        update_string = str(os.getenv('UPDATEPALLETGROUP'))
        updated_pallet_group_info = db(update_string.format(new_pallet_group_data,id))
        return updated_pallet_group_info
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def delete_pallet_group(id):
    try:
        pallet_group = db(f"{os.getenv('DELETEPALLETGROUP')}{id}")
        return pallet_group
    except Exception as ex:
        print("Data could not be processed: \n", ex)
