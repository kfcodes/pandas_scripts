from data_access_layer.read_database_functions import read_selection_to_list
from data_access_layer.write_database_functions import db, insert_db_data, update_db_data
from data_models_layer.table_models import finished_product_table

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

async def create_finished_product(product_data):
    try:
        table =  finished_product_table();
        insert_db_data(table, product_data)
        return f"inserted data into the database for: {product_data}"
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_finished_product(product_id):
    try:
        finished_product = read_selection_to_list(f"{os.getenv('GETFINISHEDPRODUCT')}'{product_id}'")
        return finished_product
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def update_finished_product(id, updated_information):
    try:
        table =  finished_product_table();
        update_db_data(table, id, updated_information)
        return updated_information
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def delete_finished_product_by_id(product_id):
    try:
        finished_product_info = read_selection_to_list(f"{os.getenv('DELETEFINISHEDPRODUCT')}'{product_id}'")
        return finished_product_info
    except Exception as ex:
        print("Data could not be processed: \n", ex)
