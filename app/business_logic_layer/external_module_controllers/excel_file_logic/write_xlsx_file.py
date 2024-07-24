import pandas as pd

import os
from dotenv import load_dotenv
load_dotenv("../../.server_config_files/fastAPI.env")

def write_data(data):
    try:
        data.to_excel("test.xlsx")
        print("Data was written to file")
    except Exception as ex:
        print("Could not write to file file: \n", ex)
