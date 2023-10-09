import os
from dotenv import load_dotenv
load_dotenv(".env")

def create_production_label_file(label_info):
    try:
        return("LABEL CREATED")
    except Exception as ex:
        print("Data could not be processed: \n", ex)
