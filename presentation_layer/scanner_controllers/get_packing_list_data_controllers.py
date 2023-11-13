from data_access_layer.read_database_functions import read_to_dataframe, read_selected_data_to_dataframe
from presentation_layer.html_controllers.scanner_html_controllers import packing_lists_html, pallet_list_html, pallet_info_html

# from ...data_access_layer.read_database_functions import read_to_dataframe, read_selected_data_to_dataframe
# from  ...presentation_layer.html_controllers.scanner_html_controllers import packing_lists_html, pallet_list_html, pallet_info_html

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
        required_pallet_info = f"{os.getenv('SCANNERPALLETINFO')}{id}"
        pallet_info = read_selected_data_to_dataframe(required_pallet_info)
        html_data = pallet_info_html(pallet_info);
        return html_data
    except Exception as ex:
        print("Data could not be processed: \n", ex)
