from data_access_layer.read_database_functions import read_selection_to_list
from data_access_layer.write_database_functions import db

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

async def create_finished_product():
    try:
        new_finished_product_id = db(f"{os.getenv('CREATEFINISHEDPRODUCT')}")
        return new_finished_product_id
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_finished_product(product_id):
    try:
        finished_product = read_selection_to_list(f"{os.getenv('GETFINISHEDPRODUCT')}'{product_id}'")
        return finished_product
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def update_finished_product(product_id):
    try:
        updated_finished_product = db(f"{os.getenv('UPDATEFINISHEDPRODUCT')}'{product_id}'")
        return updated_finished_product
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def delete_finished_product_by_id(product_id):
    try:
        finished_product_info = read_selection_to_list(f"{os.getenv('DELETEFINISHEDPRODUCT')}'{product_id}'")
        return finished_product_info
    except Exception as ex:
        print("Data could not be processed: \n", ex)
