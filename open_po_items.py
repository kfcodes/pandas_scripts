from numpy import number
import pandas as pd
import sqlalchemy as sqlalchemy
from sql import write_pandas_dataframe_to_sql
import os
from dotenv import load_dotenv
load_dotenv(".env")

output_file = os.getenv('PO_ITEM')
df = pd.read_excel(output_file, skiprows=[0])
correct_columns.dropna();
cc = correct_columns[correct_columns.product_id.notnull()]
cc2 = correct_columns[correct_columns["product_id"].str.contains("CAR") == False]
write_pandas_dataframe_to_sql.write_to_database(cc2, 'tpoidb_table') 
