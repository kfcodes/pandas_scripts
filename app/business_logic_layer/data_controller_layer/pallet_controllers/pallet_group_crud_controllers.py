from physical_layer.data_access_layer.read_database_functions import read_selection_to_list, read_to_list_index
from physical_layer.data_access_layer.write_database_functions import db, db2

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

# CREATE THE NEW GROUP IN THE DB
async def create_new_pallet_group(name):
    try:
        create_pallet_group_info = str(os.getenv('CREATENEWPALLETGROUP'))
        result = db(create_pallet_group_info.format(str(name)))
        print(result)
        return "Created a new pallet group"
    except Exception as ex:
        print("Data could not be processed: \n", ex)

# GET THE DETAILS OF THE INDIVIDUAL PALLET GROUP
async def get_pallet_group_info(id):
    try:
        pallet_group = read_to_list_index(f"{os.getenv('GETPALLETGROUPINFO')}'{int(id)}'")
        return pallet_group
    except Exception as ex:
        print("Data could not be processed: \n", ex)

# UPDATE THE DETAILS OF THE INDIVIDUAL PALLET GROUP
async def update_pallet_group(id, new_pallet_group_data):
    try:
        new_pallet_group_data = str(new_pallet_group_data).replace(' ', ' ,').replace('None', 'Null')
        update_string = str(os.getenv('UPDATEPALLETGROUP'))
        updated_pallet_group_info = db(update_string.format(new_pallet_group_data,id))
        return updated_pallet_group_info
    except Exception as ex:
        print("Data could not be processed: \n", ex)

#  DELETE PALLET GROUP
async def delete_pallet_group(id):
    try:
        pallet_group = db(f"{os.getenv('DELETEPALLETGROUP')}{id}")
        return pallet_group
    except Exception as ex:
        print("Data could not be processed: \n", ex)
