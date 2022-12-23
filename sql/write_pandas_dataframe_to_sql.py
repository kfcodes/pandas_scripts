import sqlalchemy as sqlalchemy
import db_connection
import os
from dotenv import load_dotenv
load_dotenv(".env")

def write_to_database(pandas_dataframe, database_table):
    try:
    # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        engine = db_connection.database_connection()
        pandas_dataframe.to_sql(os.getenv(database_table), engine, if_exists='append', index=False)
        print("Data was inserted into the database")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
