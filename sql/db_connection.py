import sqlalchemy as sqlalchemy
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv(".env")

connection_credentials = {'usr': os.getenv("USR"),
        'pwd': os.getenv("PASSWORD"),
        'hst': os.getenv("HOST"),
        'prt': os.getenv("PORT"),
        'dbn': os.getenv("DATABASE")}

#connection_string = 'mysql+mysqlconnector://{usr}:{pwd}@{hst}:{prt}/{dbn}'
connection_string = 'mariadb+pymysql://{usr}:{pwd}@{hst}:{prt}/{dbn}'

# Create Database Connection
def database_connection():
    return create_engine(connection_string.format(**connection_credentials))
