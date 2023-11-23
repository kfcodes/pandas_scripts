from data_access_layer.read_database_functions import read_selection_to_list

import os
from dotenv import load_dotenv
load_dotenv("../.env")

async def create_finished_product():
    try:
        finished_product_id = read_selection_to_list(f"{os.getenv('')}")
        return finished_product_id
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_finished_product_by_id(id):
    try:
        finished_product = read_selection_to_list(f"{os.getenv('')}'{id}'")
        return finished_product
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def update_finished_product_by_id(id):
    try:
        finished_product = read_selection_to_list(f"{os.getenv('')}'{id}'")
        return finished_product
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def delete_finished_product_by_id(id):
    try:
        finished_product = read_selection_to_list(f"{os.getenv('')}'{id}'")
        return finished_product
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_finished_product_group(group_id):
    try:
        finished_products = read_selection_to_list(f"{os.getenv('')}'{group_id}'")
        return finished_products
    except Exception as ex:
        print("Data could not be processed: \n", ex)
