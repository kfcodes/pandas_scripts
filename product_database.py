# Write the processed data to db
import pandas as pd
import sqlalchemy as sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import mysql.connector
import db_connection
import os
from dotenv import load_dotenv
load_dotenv(".env")

database_output_file = os.getenv('DATABASE_FILE')

sage_dataframe = pd.read_excel(database_output_file)

sage_column_data = sage_dataframe.loc[:, [ os.getenv('Column1'), os.getenv('Column2'), os.getenv('Column3'), os.getenv('Column4')]]

correct_column_names = sage_column_data.rename(columns={os.getenv('Column1'):os.getenv('Column_1'),os.getenv('Column2'):os.getenv('Column_2'),os.getenv('Column3'):os.getenv('Column_3'),os.getenv('Column4'):os.getenv('Column_4'),})

correct_column_names[os.getenv('Column_1')] = correct_column_names[os.getenv('Column_1')].str.lower()
correct_column_names[os.getenv('Column_2')] = correct_column_names[os.getenv('Column_2')].str.lower()

engine = db_connection.create_connection()
correct_column_names.to_sql(os.getenv('pdb_table'), engine, if_exists='append', index=False)

