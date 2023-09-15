import os
from dotenv import load_dotenv
load_dotenv("../.env")
from database.read_db_index import get_production_info, get_database_info2

def get_component_data(id):
    try:
        product = f"{os.getenv('PRODUCTIONINFO')}{id}"
        uid, q, w, e, r, p = get_production_info(product)
        print(f"id: {uid}")
        print(f"description: {q}")
        print(f"lot: {w}")
        print(f"bbe: {e}")
        print(f"order_id: {r}")
        print(f"orderQty: {p}")

    except Exception as ex:
        print("Data could not be processed: \n", ex)

get_component_data("18")
