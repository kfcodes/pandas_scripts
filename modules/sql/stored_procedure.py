import os
from dotenv import load_dotenv
load_dotenv(".env")
import pandas as pd
from connect import database_connection
import sqlalchemy as sqlalchemy

def call_stored_function(name):
    try:
    except Exception as ex:
print("Connection could not be made due to the following error: \n", ex)
