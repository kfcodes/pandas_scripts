from physical_layer.data_access_layer.read_database_functions import read_selection_to_list, read_to_list_index
from physical_layer.data_access_layer.write_database_functions import db, db2

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

# CREATE NEW PACKING LIST
async def create_new_packing_list(name):
    try:
        create_packing_list = str(os.getenv('CREATENEWPACKINGLIST'))
        response = db(create_packing_list.format(str(name)))
        print(response)
        return f"Created new packing list {name}"
    except Exception as ex:
        print("Data could not be processed: \n", ex)

# GET SUMMARY INFORMATION ABOUT THE PACKING LIST
async def get_packing_list_info(id):
    try:
        get_packing_list_info = str(os.getenv('GETPACKINGLISTINFO'))
        packing_list_info = read_to_list_index(get_packing_list_info.format(int(id)))
        return packing_list_info
    except Exception as ex:
        print("Data could not be processed: \n", ex)

# UPDATE THE NAME OF A PACKING LIST
async def update_packing_list_name(id, name):
    try:
        update_string = str(os.getenv('UPDATEPACKINGLISTNAME'))
        updated_packing_list_name = db(update_string.format(str(name), int(id)))
        return updated_packing_list_name;
    except Exception as ex:
        print("Data could not be processed: \n", ex)

# MARK A PACKING LIST AS DISPATCHED
async def dispatch_packing_list(id):
    try:
        dispatch_string = str(os.getenv('DISPATCHPACKINGLIST'))
        result = db(dispatch_string.format(int(id)))
        return result
    except Exception as ex:
        print("Data could not be processed: \n", ex)

#  DELETE PACKING LIST
async def delete_packing_list(id):
    try:
        prepare_string = str(os.getenv('PREPARETODELETEPACKINGLIST'))
        delete_string = str(os.getenv('DELETEPACKINGLIST'))
        result = db(prepare_string.format(int(id)))
        result_2 = db(delete_string.format(int(id)))
        return result, result_2
    except Exception as ex:
        print("Data could not be processed: \n", ex)
