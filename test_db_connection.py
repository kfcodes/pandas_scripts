# import pandas as pd
import pandas as pd
import sqlalchemy as sqlalchemy
from sqlalchemy import create_engine
import db_connection
import os
from dotenv import load_dotenv
load_dotenv(".env")

try:
# GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
    engine = db_connection.database_connection()
    test_table = pd.read_sql(os.getenv('test_table'),engine)
    print(test_table)
except Exception as ex:
    print("Connection could not be made due to the following error: \n", ex)
