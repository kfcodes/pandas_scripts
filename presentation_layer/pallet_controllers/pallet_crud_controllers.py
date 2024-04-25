from data_access_layer.write_database_functions import db
from data_access_layer.read_database_functions import read_selection_to_list, read_to_list_index
from business_logic_layer.zpl_logic_module.pallet_labels.combined_pallet_label import create_combined_pallet_label_outline, create_combined_pallet_label_data
from business_logic_layer.print_logic_module.print_zpl import print_large_label

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

async def update_pallet(id, new_pallet_data):
    try:
        new_pallet_data = str(new_pallet_data).replace(' ', ' ,').replace('None', 'Null')
        update_string = str(os.getenv('UPDATEPALLET'))
        updated_pallet_info = db(update_string.format(new_pallet_data,id))
        return updated_pallet_info
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def delete_pallet(id):
    try:
        pallet = db(f"{os.getenv('DELETEPALLET')}{id}")
        return pallet
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def combine_pallets_import(pallet_id ,height, pallet_list):
    try:
        update_string = str(os.getenv('COMBINEPALLETDATA'))
        update_pallets_response = db(update_string.format(pallet_id, height, pallet_list))
        print(update_pallets_response)
        sql = str(os.getenv('GETCOMBINEDPALLETDATA'))
        combined_label_outline = create_combined_pallet_label_outline()
        combined_pallet_data = read_to_list_index(sql.format(pallet_id))
        ids = str(pallet_list)
        ids = ids.replace("(","")
        ids = ids.replace(")","")
        ids = ids.replace("'","")
        combined_label_body = create_combined_pallet_label_data(combined_pallet_data[0], ids)
        label_data = str(combined_label_outline) + str(combined_label_body)
        response = print_large_label(label_data)
        return response
    except Exception as ex:
        print("Data could not be processed: \n", ex)
