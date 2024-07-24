from sqlalchemy import create_engine

import os
from dotenv import load_dotenv
load_dotenv("../../.server_config_files/fastAPI.env")

usr = os.getenv("USR")
pwd = os.getenv("PASSWORD")
hst = os.getenv("HOST")
prt = os.getenv("PORT")
db = os.getenv("DATABASE")

connection_string = f'mariadb+pymysql://{usr}:{pwd}@{hst}:{prt}/{db}'

def database_connection():
    engine = create_engine(connection_string)
    return engine;
