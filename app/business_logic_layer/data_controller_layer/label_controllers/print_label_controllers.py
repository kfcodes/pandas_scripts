from physical_layer.data_access_layer.read_database_functions import get_label_data, read_to_list_index
from business_logic_layer.external_module_controllers.zpl_logic.product_box_logic.small_type_1_box_label import create_small_label_data,  create_small_label_outline
from business_logic_layer.external_module_controllers.zpl_logic.pallet_logic.generic_pallet_label import create_pallet_label_outline, create_pallet_label_data, add_products_to_label
from business_logic_layer.external_module_controllers.zpl_logic.internal_logic.internal_pallet_label import create_blank_label_outline
from business_logic_layer.external_module_controllers.print_logic.print_zpl import print_small_label, print_large_label, print_specific_label
import business_logic_layer.external_module_controllers.zpl_logic.product_box_logic.large_type_1_box_label as label_type_1
import business_logic_layer.external_module_controllers.zpl_logic.product_box_logic.large_type_2_box_label as label_type_2
import business_logic_layer.external_module_controllers.zpl_logic.product_box_logic.large_type_3_box_label as label_type_3
import business_logic_layer.external_module_controllers.zpl_logic.product_box_logic.large_type_4_box_label as label_type_4
import business_logic_layer.external_module_controllers.zpl_logic.product_box_logic.small_type_2_box_label as type_2_label
import business_logic_layer.external_module_controllers.zpl_logic.product_box_logic.large_type_5_box_label as label_type_5

import os
from dotenv import load_dotenv
load_dotenv("../../.server_config_files/fastAPI.env")

async def print_pallet_label(id):
    try:
        label_info_string = str(f"{os.getenv('PALLETLABELPART1')}")
        label_info = read_to_list_index(label_info_string.format(int(id),int(id)))
        print("label_info", label_info)
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

async def print_large_product_label(id, quantity, quantity_in_a_box, exp):
    try:
        label_info = read_to_list_index(f"{os.getenv('PRODUCTIONLABELINFO')}{id}")
        label_type = label_info[0][f'{os.getenv("LABELFIELD20")}']
        label_info = label_info[0]

        if label_type == 1:
            outline = label_type_1.create_large_product_label_outline()
            body = label_type_1.create_large_product_label_data(label_info, quantity, quantity_in_a_box, exp)
            print(body)
            label_data = outline + body
            response = print_large_label(label_data)

        elif label_type == 2:
            outline = label_type_2.create_large_product_label_outline()
            body = label_type_2.create_large_product_label_data(label_info, quantity, quantity_in_a_box, exp)
            print(body)
            label_data = outline + body
            response = print_large_label(label_data)

        elif label_type == 3:
            outline = label_type_3.create_large_product_label_outline()
            body = label_type_3.create_large_product_label_data(label_info, quantity, quantity_in_a_box, exp)
            print(body)
            label_data = outline + body
            response = print_large_label(label_data)

        elif label_type == 4:
            outline = label_type_4.create_large_product_label_outline()
            body = label_type_4.create_large_product_label_data(label_info, quantity, quantity_in_a_box, exp)
            label_data = outline + body
            print(label_info)
            response = print_large_label(label_data)

        else:
            response = {"message" : "No label Data for this label"}

        return response

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

async def print_this_label(qty):
    try:
        print("data_layer")
        label_outline = type_2_label.create_this_label(qty)
        print("print_label_data")
        print(label_outline)
        response = print_small_label(label_outline)
        return response
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def print_specific_label_now():
    try:
        label_outline = f"""
        ^XA
        ^CF0,80
        TEST
        ^XZ"""
        response = print_specific_label(label_outline)
        return response
    except Exception as ex:
        print("Data could not be processed: \n", ex)

# THIS IS THE FUNCTION TO PRINT THE NEW PRODUCT LABELS
async def print_specific_label_now_2(id):
    try:
        label_info = read_to_list_index(f"{os.getenv('TESTNEWLABEL')}'{id}'")
        label_outline = label_type_5.create_large_product_label_2(label_info[0])
        print(label_outline)
        response = print_specific_label(label_outline)
        return response
    except Exception as ex:
        print("Data could not be processed: \n", ex)
