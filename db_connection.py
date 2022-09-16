import pandas as pd
import sqlalchemy as sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv(".env")
# Create Database Connection
creds = {'usr': os.environ.get("USR"),
        'pwd': os.environ.get("PASSWORD"),
        'hst': os.environ.get("HOST"),
        'prt': os.environ.get("PORT"),
        'dbn': os.environ.get("DATABASE")}
connstr = 'mysql+mysqlconnector://{usr}:{pwd}@{hst}:{prt}/{dbn}'
# engine = create_engine(connstr.format(**creds))

 # PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
 # RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    return create_engine(connstr.format(**creds))
    # create_engine(
        # url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
        # creds[usr], pwd, hst, prt, dbn
        # )
        # )

