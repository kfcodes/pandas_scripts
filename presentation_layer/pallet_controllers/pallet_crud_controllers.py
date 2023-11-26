from data_access_layer.read_database_functions import read_selection_to_list
from data_access_layer.write_database_functions import db

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

async def create_pallet():
    try:
        db(f"{os.getenv('CREATEPALLET')}")
        pallet_id = read_selection_to_list(f"{os.getenv('GETNEWPALLETID')}")
        new_pallet_id = pallet_id['pallet_id'][0]
        return new_pallet_id
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_pallet(id):
    try:
        pallet = read_selection_to_list(f"{os.getenv('GETPALLET')}'{id}'")
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

async def combine_pallets():
    try:
        pallets = db(f"{os.getenv('')}'{id}'")
        return pallets
    except Exception as ex:
        print("Data could not be processed: \n", ex)
