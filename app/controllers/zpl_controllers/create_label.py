import os
from dotenv import load_dotenv
load_dotenv("../../../.env")

def create_label(label_info):
    try:
        print(label_info)
        return("LABEL CREATED")
    except Exception as ex:
        print("Data could not be processed: \n", ex)