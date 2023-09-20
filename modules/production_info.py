import pprint
import os
from dotenv import load_dotenv
load_dotenv("../.env")
from database.read_db_index import get_production_info, get_production_components

def get_component_data(id):
    try:
        pp = pprint.PrettyPrinter(indent=4)
        product = f"{os.getenv('PRODUCTIONINFO')}{id}"
        product_info = get_production_info(product)
        uid = product_info[os.getenv("UID")][0]
        production_components = f"{os.getenv('COMPONENTS')}'{uid}'"
        pp.pprint(production_components)

    except Exception as ex:
        print("Data could not be processed: \n", ex)

get_component_data("3")
