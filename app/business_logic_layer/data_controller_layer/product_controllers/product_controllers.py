from physical_layer.data_access_layer.read_database_functions import read_selection_to_list, read_to_list_index
import os
from dotenv import load_dotenv
load_dotenv(".env")

async def get_all_products():
    try:
        products_list = read_selection_to_list(f"{os.getenv('GETALLPRODUCTS')}")
        return products_list
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_all_finished_products():
    try:
        products_list = read_selection_to_list(f"{os.getenv('GETALLFINISHEDPRODUCTS')}")
        return products_list
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_product_by_id(id):
    try:
        product_info = read_to_list_index(f"{os.getenv('GETPRODUCTBYID')}'{id}'")
        return product_info[0]
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_finished_product_by_id(id):
    try:
        finished_product = read_selection_to_list(f"{os.getenv('GETFINISHEDPRODUCTBYID')}'{id}'")
        return finished_product
    except Exception as ex:
        print("Data could not be processed: \n", ex)
