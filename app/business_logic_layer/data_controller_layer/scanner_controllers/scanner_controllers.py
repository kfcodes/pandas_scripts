# from physical_layer.data_access_layer.read_database_functions import read_to_dataframe, read_selected_data_to_dataframe, read_selection_to_list
# from physical_layer.data_access_layer.write_database_functions import db
# from business_logic_layer.external_module_controllers.html_logic.scanner_html_components #import packing_lists_html, pallet_list_html, pallet_info_html

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

def get_all_packing_lists():
    try:
        packing_lists = read_to_dataframe('PACKINGLISTS')
        html_data = packing_lists_html(packing_lists);
        return html_data
    except Exception as ex:
        print("Data could not be processed: \n", ex)

def get_packing_list(id):
    try:
        required_pallets = f"{os.getenv('SCANNERPALLETS')}{id}"
        pallets = read_selected_data_to_dataframe(required_pallets)
        html_data = pallet_list_html(pallets);
        return html_data
    except Exception as ex:
        print("Data could not be processed: \n", ex)

def get_pallet_info(id):
    try:
        id = str(id).split('=')
        body_id_2 = id[1].split("'")
        id = body_id_2[0]
        required_pallet_info = f"{os.getenv('SCANNERPALLETINFO')}{id}"
        pallet_info = read_selected_data_to_dataframe(required_pallet_info)
        html_data = pallet_info_html(pallet_info);
        return html_data
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def load_pallet_and_get_packing_list(id):
    try:
        packing_list = f"{os.getenv('PACKINGLISTPALLETS')}{id}"
        packing_list_id = read_selection_to_list(packing_list)
        packing_list_id = packing_list_id['packing_list'][0]
        dispatched_pallet_sql = f"{os.getenv('PALLETDISPATCHED')}{id}"
        db(dispatched_pallet_sql)
        return packing_list_id
    except Exception as ex:
        print("Data could not be processed: \n", ex)
