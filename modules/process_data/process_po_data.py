import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv("../.env")

def process_data(data):
    try:
        print(data)
        test="test"
        test2="test2"
        return(test, test2);
    except Exception as ex:
        print("Data could not be processed: \n", ex)


