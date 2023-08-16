import os
from dotenv import load_dotenv
load_dotenv(".env")
import pandas as pd
from db_connection import database_connection
import sqlalchemy as sqlalchemy

def write_to_database(data, name):
    try:
        data.to_sql(os.getenv(name), database_connection(), if_exists='append', index=False)
        print("Data was inserted into the database")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
