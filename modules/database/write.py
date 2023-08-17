import os
from dotenv import load_dotenv
load_dotenv("../../.env")
from .connect import database_connection

def write_to_database(data, name):
    try:
        data.to_sql(os.getenv(name), database_connection(),if_exists='append', index=False)
        print("Data was inserted into database")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
