from physical_layer.data_access_layer.read_database_functions import read_selection_to_list

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

async def get_all_brands():
    try:
        brands = read_selection_to_list(f"{os.getenv('GETALLBRANDS')}")
        return brands
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_products_from_brand(brand_id):
    try:
        products = read_selection_to_list(f"{os.getenv('GETPRODUCTSFROMBRAND')}'{brand_id}%'")
        return products
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_assembly_information(product_id):
    try:
        assembly_information = read_selection_to_list(f"{os.getenv('GETASSEMBLYINFORMATION')}'{product_id}'")
        return assembly_information
    except Exception as ex:
        print("Data could not be processed: \n", ex)
