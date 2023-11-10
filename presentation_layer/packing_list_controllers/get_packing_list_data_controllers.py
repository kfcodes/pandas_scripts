from fastapi.responses import HTMLResponse
# from data_access_layer.read_database_functions import read_to_dataframe
# from business_logic_layer.html_controllers.create_scanner_html import create_packing_list_html
from ...data_access_layer.read_database_functions import read_to_dataframe
from ...business_logic_layer.html_controllers.create_scanner_html import packing_lists_html, pallet_list_html, pallet_info_html

def get_all_packing_lists():
    try:
        packing_lists = read_to_dataframe('PACKINGLISTS')
        html_data = packing_lists_html(packing_lists);
        return html_data
    except Exception as ex:
        print("Data could not be processed: \n", ex)

def get_packing_list(id):
    try:
        pallets = read_to_dataframe('PALLETS')
        html_data = pallet_list_html(pallets);
        return html_data
    except Exception as ex:
        print("Data could not be processed: \n", ex)

def get_pallet_info(id):
    try:
        pallet_info = read_to_dataframe('PACKINGLISTS')
        html_data = pallet_info_html(pallet_info);
        return html_data

    except Exception as ex:
        print("Data could not be processed: \n", ex)

