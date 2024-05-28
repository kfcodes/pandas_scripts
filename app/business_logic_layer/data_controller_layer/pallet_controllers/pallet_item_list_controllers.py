import os
from data_access_layer.read_database_functions import read_to_list_index

async def get_all_pallet_items():
    try:
        resultlist = [];
        pallet_items = read_to_list_index(f"{os.getenv('GETALLPALLETITEMS')}")
        for key, val in pallet_items.items():
            resultlist.append(val)
        return resultlist;
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_new_pallet_items():
    try:
        resultlist = [];
        pallet_items = read_to_list_index(f"{os.getenv('GETNEWPALLETITEMS')}")
        for key, val in pallet_items.items():
            resultlist.append(val)
        return resultlist;
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def find_pallet_items_for_pallet_function(id):
    try:
        resultlist = [];
        pallet_items = read_to_list_index(f"{os.getenv('GETNPALLETITEMSFORPALLET')}{id}")
        for key, val in pallet_items.items():
            resultlist.append(val)
        return resultlist;
    except Exception as ex:
        print("Data could not be processed: \n", ex)

