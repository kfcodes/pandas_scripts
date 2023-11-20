from data_access_layer.read_database_functions import get_label_data
from business_logic_layer.zpl_controllers.create_small_label import create_small_label_data,  create_small_label_outline
from business_logic_layer.zpl_controllers.create_large_product_label import create_large_product_label_data,  create_large_product_label_outline
from business_logic_layer.zpl_controllers.create_large_pallet_label import create_pallet_label_data_part_1, create_pallet_label_data_part_2, create_pallet_label_outline
from business_logic_layer.print_controllers.print_zpl import print_small_label, print_large_label

import os
from dotenv import load_dotenv
load_dotenv("../.env")

async def print_small_product_label(id):
    try:
        label_info = get_label_data(f"{os.getenv('PRODUCTIONLABELINFO')}{id}")
        outline = create_small_label_outline()
        body = create_small_label_data(label_info, 1)
        label_data = outline + body
        print(label_data)
        # print_small_label(label_data)
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def print_large_product_label(id):
    try:
        label_info = get_label_data(f"{os.getenv('PRODUCTIONLABELINFO')}{id}")
        outline = create_large_product_label_outline()
        body = create_large_product_label_data(label_info, 1)
        label_data = outline + body
        print_large_label(label_data)
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def print_pallet_label(id):
    try:
        label_info = get_label_data(f"{os.getenv('PALLETLABELPART1')} {int(id)} {os.getenv('PALLETLABELPART2')}")
        outline = create_pallet_label_outline()
        body = create_pallet_label_data_part_1(label_info)
        body_2 = create_pallet_label_data_part_2(label_info)
        label_data = outline + body
        # data = await print_pallet_label(label_data)
        # print(data)

        # return f"printed pallet label for {id}"
        return label_data
    except Exception as ex:
        print("Data could not be processed: \n", ex)
