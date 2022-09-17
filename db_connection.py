import pandas as pd
import sqlalchemy as sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv(".env")

connection_credentials = {'usr': os.getenv("USR"),
        'pwd': os.getenv("PASSWORD"),
        'hst': os.getenv("HOST"),
        'prt': os.getenv("PORT"),
        'dbn': os.getenv("DATABASE")}

connection_string = 'mysql+mysqlconnector://{usr}:{pwd}@{hst}:{prt}/{dbn}'

# Create Database Connection
def create_connection():
    return create_engine(connection_string.format(**connection_credentials))
