# import pandas as pd
import pandas as pd
import sqlalchemy as sqlalchemy
import db_connection
import os
from dotenv import load_dotenv
load_dotenv(".env")

def read_database(database_table):
    try:
    # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        engine = db_connection.database_connection()
        sql_table = pd.read_sql(os.getenv(database_table),engine)
        print(sql_table)
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
