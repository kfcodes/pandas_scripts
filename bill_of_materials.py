import pandas as pd
import sqlalchemy as sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import mysql.connector
import db_connection
import os
import csv
from dotenv import load_dotenv
load_dotenv(".env")

path = os.getenv('BOM_PATH')

for root, directories, filea in os.walk(path):
    for file in filea:
        if file.endswith(".xlsx"):
            file_name, file_name_extension = os.path.splitext(file)
            df = pd.read_excel(os.path.join(root,file))
            bom_name_row = df.loc[df.Type == 'Bill of Materials'].values[0]
            bom_name = bom_name_row.tolist()[0]
            print(bom_name)
            subassembly_row = df.loc[df.Type == 'Subassembly'].values[0]
            subassembly_quantity = subassembly_row.tolist()[2]
            print(subassembly_quantity)
            subassembly_code = subassembly_row.tolist()[0]
            print(subassembly_code)
