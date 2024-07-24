from physical_layer.data_access_layer.read_database_functions import read_selection_to_list, read_to_list_index
from physical_layer.data_access_layer.write_database_functions import db, insert_db_data, update_db_data
from physical_layer.data_models_layer.table_models import finished_product_table
from physical_layer.data_models_layer.object_models import Finished_product

import os
from dotenv import load_dotenv
load_dotenv("../../.server_config_files/fastAPI.env")

async def create_finished_product(product_data):
    try:
        new_item_data = str(product_data).replace(' ', ' ,').replace('None', 'Null')
        create_finished_product_string = f"{os.getenv('CREATEFINISHEDPRODUCT')}{new_item_data}"
        create_finished_product_string = create_finished_product_string.replace("eol_id=Null ,", "")
        db(create_finished_product_string)
        product = read_selection_to_list(f"{os.getenv('GETNEWESTPRODUCTID')}")
        new_finished_product_id = product['eol_id'][0]
        return new_finished_product_id
    except Exception as ex:
        print("Data could not be processed: \n", ex)

async def get_finished_product(product_id):
    try:
        finished_product = read_to_list_index(f"{os.getenv('GETFINISHEDPRODUCT')}'{product_id}'")
        return_product = []
        return_product.append(finished_product[0])
        return return_product
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
