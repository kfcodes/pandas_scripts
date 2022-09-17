import pandas as pd
import sqlalchemy as sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv(".env")
# Create Database Connection
creds = {'usr': 'root',
        'pwd': 'p',
        'hst': '127.0.0.1',
        'prt': '3306',
        'dbn': 'test'}
creds2 = {'usr': os.getenv("USR"),
        'pwd': 'p',
        'hst': os.getenv("HOST"),
        'prt': os.getenv("PORT"),
        'dbn': os.getenv("DATABASE")}
connstr = 'mysql+mysqlconnector://{usr}:{pwd}@{hst}:{prt}/{dbn}'
# # engine = create_engine(connstr.format(**creds))
# # brand_prefix = pd.read_sql('brand', engine, columns = ["prefix"], index_col="name")
# # print(brand_prefix)

#  # PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
#  # RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
# engine = create_engine(connstr.format(**creds))
    # return create_engine(connstr.format(**creds))
    return create_engine(connstr.format(**creds2))
    # return create_engine(connstr = 'mysql+mysqlconnector://{usr}:{pwd}@{hst}:{prt}/{dbn}')
    print(creds)
    print(creds2)

if __name__ == '__main__':
    try:
    # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        engine = get_connection()
        brand_prefix = pd.read_sql('brand', engine)
        print(brand_prefix)
        # print(f"Connection to the {hst} for user {usr} created successfully.")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

# Create Database Connection 
