from physical_layer.data_access_layer.read_database_functions import read_selection_to_list, read_to_list_index
from physical_layer.data_access_layer.write_database_functions import db, db2

import os
from dotenv import load_dotenv
load_dotenv(".env")

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

async def get_pallet_summary(like, lot):
    try:
        # print(like)
        like = str(like)
        # print(lot)
        lot = str(lot)
        pallet_summary = str(os.getenv('SUMMARY_1'))
        # print(update_string)
        products_string = pallet_summary.format(like,lot)
        # print(products_string)
        products = db2(products_string)
        # products = products.mappings().all()
        # print(products)
        product_list = [];
        previous_product = "";
        for item in products:
            # print(list(item))
            item = item._asdict()
            print(item)
            if (item["product_id"] == previous_product): 
                item["product_description"] = None
                item["product_id"] = None
            else:
                previous_product = item["product_id"]
            product_list.append(item)
        return product_list
        print(products)
        # return "product_list"
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_pallet_data():
    try:
        pallets = read_to_list_index(f"{os.getenv('GETPALLETDATA')}")
        print(pallets)
        pallet_list = [];
        previousPallet = "0";
        for key, item in pallets.items():
            print(item)
            if (item["PALLET"] == previousPallet): 
                item["WEIGHT"] = None
                item["DIMENSIONS"] = None
                item["PALLET"] = None
            else:
                previousPallet = item["PALLET"]
            # if (item["PALLET"] == previousPallet): 
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

async def get_open_pallet_groups():
    try:
        pallets = read_selection_to_list(f"{os.getenv('GETOPENPALLETLISTS')}")
        return pallets
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_open_pallets():
    try:
        pallets = read_selection_to_list(f"{os.getenv('GETOPENPALLETS')}")
        return pallets
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_packing_list_pallets():
    try:
        pallets = read_selection_to_list(f"{os.getenv('GETPACKINGLISTPALLETS')}")
        return pallets
    except Exception as ex:
        print("Data could not be processed: \n", ex)
