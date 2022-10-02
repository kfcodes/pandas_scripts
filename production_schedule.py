# Created production schedule file that connects to db
import pandas as pd
import sqlalchemy as sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import mysql.connector
import db_connection
import os
from dotenv import load_dotenv
load_dotenv(".env")

try:
# GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
    engine = db_connection.create_connection()
    test_table = pd.read_sql(os.getenv('test_table'),engine)
    print(test_table)
except Exception as ex:
    print("Connection could not be made due to the following error: \n", ex)
