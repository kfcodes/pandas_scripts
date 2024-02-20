from data_access_layer.read_database_functions import get_label_data, read_to_list_index
from business_logic_layer.zpl_logic_module.create_small_label import create_small_label_data,  create_small_label_outline
from business_logic_layer.zpl_logic_module.create_pallet_label import create_pallet_label_outline, create_pallet_label_data, add_products_to_label
from business_logic_layer.zpl_logic_module.create_blank_label import create_blank_label_outline
from business_logic_layer.print_logic_module.print_zpl import print_small_label, print_large_label
from business_logic_layer.zpl_logic_module.create_large_product_label_2 import create_large_product_label_data,  create_large_product_label_outline
# from business_logic_layer.zpl_logic_module.create_large_product_label import create_large_product_label_data,  create_large_product_label_outline

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

async def print_pallet_label(id):
    try:
        label_info = get_label_data(f"{os.getenv('PALLETLABELPART1')}{int(id)}")
        outline = create_pallet_label_outline()
        pallet_products = read_to_list_index(f"{os.getenv('GETPRODUCTSONPALLET1')} {int(id)} {os.getenv('GETPRODUCTSONPALLET2')}")
        products = add_products_to_label(pallet_products)
        body = create_pallet_label_data(label_info[0])
        label_data = outline + products + body
        response = print_large_label(label_data)
        return response
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def print_small_product_label(id):
    try:
        label_info = read_to_list_index(f"{os.getenv('PRODUCTIONLABELINFO')}{id}")
        outline = create_small_label_outline()
        body = create_small_label_data(label_info, 1)
        label_data = outline + body
        response = print_small_label(label_data)
        return response
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def print_large_product_label(id, quantity, quantity_in_a_box):
    try:
        label_info = read_to_list_index(f"{os.getenv('PRODUCTIONLABELINFO')}{id}")
        label_data = label_info[0]
        # print(label_info)
        # print(label_info[{os.getenv("LABELFIELD18")}])
        # if label_info[{os.getenv("LABELFIELD18")}] != None:
        outline = create_large_product_label_outline()
        body = create_large_product_label_data(label_info[0], quantity, quantity_in_a_box)
        print(body)
        label_data = outline + body
        response = print_large_label(label_data)
        return response
        # else:
        #     return {"message" : "No label Data"}
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def print_blank_pallet_label():
    try:
        label_outline = create_blank_label_outline()
        response = print_large_label(label_outline)
        return response
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def print_combined_pallet_label(data):
    try:
        label_info = str(data["label_info"])
        response = print_large_label(label_info)
        return response
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_label_info(id):
    try:
        label_info_list = [];
        label_info = get_label_data(f"{os.getenv('GETLABELINFO')}'{id}'");
        label_info_list.append(label_info[0]);
        return label_info_list;
    except Exception as ex:
        print("Data could not be processed: \n", ex)
