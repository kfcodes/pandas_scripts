# Added functionality to import and process xlsx files with BOM data
import pandas as pd
import sqlalchemy as sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import mysql.connector
import db_connection
import os
import csv
from dotenv import load_dotenv
load_dotenv(".env")

path = os.getenv("BOM_PATH")

for root, directories, filea in os.walk(path):
    for file in filea:
        if file.endswith(".xlsx"):
            file_name, file_name_extension = os.path.splitext(file)
            df = pd.read_excel(os.path.join(root,file))
            print(df)
