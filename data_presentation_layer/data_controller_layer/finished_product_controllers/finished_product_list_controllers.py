from data_access_layer.read_database_functions import read_selection_to_list
from data_access_layer.write_database_functions import db

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

async def get_finished_product_group(group_id):
    try:
        finished_products = read_selection_to_list(f"{os.getenv('FINISHEDPRODUCTGROUP')}'{group_id}'")
        return finished_products
    except Exception as ex:
        print("Data could not be processed: \n", ex)
