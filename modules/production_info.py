import os
from dotenv import load_dotenv
load_dotenv("../.env")
import pandas as pd
from database.read_db_index import get_production_info, get_database_info2
import pprint
pp = pprint.PrettyPrinter(indent=4)

def get_component_data(id):
    try:
        product = f"{os.getenv('PRODUCTIONINFO')}{id}"
        product_info = get_production_info(product)
        uid = product_info[os.getenv("UID")][0]
        production_components = f"{os.getenv('COMPONENTS')}'{uid}'"
        components = get_database_info2(production_components);
        print(f" Components: {components}")

    except Exception as ex:
        print("Data could not be processed: \n", ex)

get_component_data("18")
