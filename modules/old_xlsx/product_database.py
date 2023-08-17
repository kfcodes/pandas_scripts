from numpy import number
import pandas as pd
import sqlalchemy as sqlalchemy
from sql import write_pandas_dataframe_to_sql
import os
from dotenv import load_dotenv
load_dotenv(".env")

database_output_file = os.getenv('DATABASE_FILE')

product_database_dataframe = pd.read_excel(database_output_file)

sage_column_data = product_database_dataframe.loc[:, [ os.getenv('Column1'), os.getenv('Column2'), os.getenv('Column3'), os.getenv('Column4')]]

correct_column_names = sage_column_data.rename(columns={os.getenv('Column1'):os.getenv('Column_1'),os.getenv('Column2'):os.getenv('Column_2'),os.getenv('Column3'):os.getenv('Column_3'),os.getenv('Column4'):os.getenv('Column_4'),})

# This is the product Description column
# correct_column_names[os.getenv('Column_1')] = correct_column_names[os.getenv('Column_1')].str.lower()
# correct_column_names[os.getenv('Column_2')] = correct_column_names[os.getenv('Column_2')].str.lower()

# I want to get the char count for the columns then get the max of that number
# correct_column_names['Description_Length'] = correct_column_names[os.getenv('Column_1')].str.len()
#
# print(correct_column_names['Description_Length']);
# print(correct_column_names['Description_Length'].max());

write_pandas_dataframe_to_sql.write_to_database(correct_column_names, 'tpdb_table')
