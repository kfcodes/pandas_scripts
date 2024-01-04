from data_access_layer.read_database_functions import read_selection_to_list, read_to_list_index
from data_access_layer.write_database_functions import db

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

async def create_pallet():
    try:
        db(f"{os.getenv('CREATENEWPALLET')}")
        pallet_id = read_selection_to_list(f"{os.getenv('GETNEWESTPALLETID')}")
        newest_pallet_id = pallet_id['pallet_id'][0]
        return newest_pallet_id
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_pallet(id):
    try:
        pallet = read_to_list_index(f"{os.getenv('GETPALLET')}'{int(id)}'")
        return pallet
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def update_pallet(id):
    try:
        pallet = db(f"{os.getenv('UPDATEPALLET')}'{id}'")
        return pallet
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def delete_pallet(id):
    try:
        pallet = db(f"{os.getenv('DELETEPALLET')}{id}")
        return pallet
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def combine_pallets_import(pallet_list, height):
    try:
        pallets = db(f"{os.getenv('')}'{id}'")
        return pallets
    except Exception as ex:
        print("Data could not be processed: \n", ex)
