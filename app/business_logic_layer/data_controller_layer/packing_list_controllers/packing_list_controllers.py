from physical_layer.data_access_layer.read_database_functions import read_selection_to_list, read_to_list_index
from physical_layer.data_access_layer.write_database_functions import db, db2
from fastapi.encoders import jsonable_encoder

import os
from dotenv import load_dotenv
load_dotenv(".env")

async def get_open_packing_lists():
    try:
        packing_lists_raw_data = read_to_list_index(f"{os.getenv('OPENPACKINGLISTS')}")
        packing_list_array = []
        for key, val in packing_lists_raw_data.items():
            packing_list_array.append(val)
        packing_list_array = jsonable_encoder(packing_list_array)
        return packing_list_array
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_open_packing_list_names():
    try:
        packing_list_names = read_to_list_index(f"{os.getenv('OPENPACKINGLISTNAMES')}")
        packing_list_names_arr = []
        for key, val in packing_list_names.items():
            packing_list_names_arr.append(val)
        packing_list_array = jsonable_encoder(packing_list_names_arr)
        return packing_list_array
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_pallets_not_on_a_packing_list():
    try:
        pallets = read_to_list_index(f"{os.getenv('PALLETSNOTONPACKINGLIST')}")
        return pallets;
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_packing_list_pallets(id):
    try:
        packing_list_pallets_str = str(f"{os.getenv('PACKINGLISTPALLETS')}")
        packing_list_pallets = read_to_list_index(packing_list_pallets_str.format(int(id)))
        return packing_list_pallets;
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_packing_list_summary_information(id):
    try:
        packing_list_summary_str = str(f"{os.getenv('PACKINGLISTSUMMARY')}")
        packing_list_summary = read_to_list_index(packing_list_summary_str.format(int(id)))
        packing_list_summary = packing_list_summary[0]
        return packing_list_summary;
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_picklist_status_information(id):
    try:
        picklist_status_str = str(f"{os.getenv('PICKLISTSTATUS')}")
        picklist_status_data = read_to_list_index(picklist_status_str.format(int(id)))
        picklist_status_data = picklist_status_data[0]
        return picklist_status_data;
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def set_pallet_packing_list(data):
    try:
        print("Data: %r" % data);
        set_packing_list_string = str(os.getenv('SETPACKINGLISTFORPALLET'))
        report = db(set_packing_list_string.format(int(data["packing_list_id"]), int(data["pallet_id"])))
        return report;
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_packing_list_pallet_information(id):
    try:
        packing_list_array = []
        packing_list_pallet_info_str = str(f"{os.getenv('PACKINGLISTPALLETINFO')}")
        packing_list_pallet_info = read_to_list_index(packing_list_pallet_info_str.format(int(id)))
        for key, val in packing_list_pallet_info.items():
            packing_list_array.append(val)
        packing_list_array = jsonable_encoder(packing_list_array)
        return packing_list_array
    except Exception as ex:
        print("Data could not be processed: \n", ex)
