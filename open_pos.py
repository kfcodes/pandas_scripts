from numpy import number
import pandas as pd
import sqlalchemy as sqlalchemy
from sql import write_pandas_dataframe_to_sql
import os
from dotenv import load_dotenv
load_dotenv(".env")

database_output_file = os.getenv('PO')
database_dataframe = pd.read_excel(database_output_file)

write_pandas_dataframe_to_sql.write_to_database(database_dataframe, 'tpodb_table')
