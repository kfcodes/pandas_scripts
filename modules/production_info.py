# import sys
import os
from dotenv import load_dotenv
load_dotenv("../.env")
import pandas as pd
from database.read_db_index import get_production_documentation, get_product_components

id = "test"
selection = f"{os.getenv('PRODUCTIONINFO')}{id}"
get_production_documentation(selection)
