import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv("../.env")

def process_schedule_data():
    try:
        return("processed_data")

    except Exception as ex:

        print("Data could not be processed: \n", ex)


