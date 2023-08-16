import sqlalchemy as sqlalchemy
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv("../../.env")

connection_credentials = {'usr': os.getenv("USR"),
        'pwd': os.getenv("PASSWORD"),
        'hst': os.getenv("HOST"),
        'prt': os.getenv("PORT"),
        'dbn': os.getenv("DATABASE")}

connection_string = 'mariadb+pymysql://{usr}:{pwd}@{hst}:{prt}/{dbn}'

def database_connection():
    print("Connected to the DB")
    return create_engine(connection_string.format(**connection_credentials))

