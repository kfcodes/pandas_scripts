from data_access_layer.read_database_functions import read_selection_to_list, read_to_list_index

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

async def get_recent_pallets():
    try:
        pallets = read_to_list_index(f"{os.getenv('GETRECENTPALLETS')}")
        resultlist = []
        for key, val in pallets.items():
            resultlist.append(val)
        return resultlist
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_all_pallets():
    try:
        pallets = read_to_list_index(f"{os.getenv('GETALLPALLETS')}")
        resultlist = []
        for key, val in pallets.items():
            resultlist.append(val)
        return resultlist
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_pallet_group(id):
    try:
        pallets = read_selection_to_list(f"{os.getenv('')}'{id}'")
        return pallets
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_pallet_details(id):
    try:
        pallet_details = read_to_list_index(f"{os.getenv('GETPALLETDETAILS')}'{int(id)}'")
        pallet_details_array = []
        pallet_details_array.append(pallet_details[0])
        return pallet_details_array
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_possible_pallets():
    try:
        pallets = read_selection_to_list(f"{os.getenv('')}")
        return pallets
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_pallet_data():
    try:
        pallets = read_to_list_index(f"{os.getenv('GETPALLETDATA')}")
        pallet_list = [];
        previousPallet = "0";
        for key, item in pallets.items():
            if (item["PALLET"] == previousPallet): 
                item["WEIGHT"] = None
                item["DIMENSIONS"] = None
                item["PALLET"] = None
            else:
                previousPallet = item["PALLET"]
            pallet_list.append(item)
        return pallet_list
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_latest_pallet_data():
    try:
        pallets = read_to_list_index(f"{os.getenv('GETLATESTPALLETDATA')}")
        pallet_list = []
        for key, val in pallets.items():
            pallet_list.append(val)
        return pallet_list
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_picklist():
    try:
        pallets = read_selection_to_list(f"{os.getenv('')}")
        return pallets
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_data_for_id(id):
    try:
        pallets = read_selection_to_list(f"{os.getenv('GETPALLETDATA')}{id}")
        return pallets
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_data():
    try:
        pallets = read_selection_to_list(f"{os.getenv('')}")
        return pallets
    except Exception as ex:
        print("Data could not be processed: \n", ex)
