import pandas as pd
import sqlalchemy as sqlalchemy
import os
from dotenv import load_dotenv
load_dotenv("../../.env")

database_output_file = os.getenv('DATABASE_FILE')
dataframe = pd.read_excel(database_output_file)

database_data = dataframe.loc[:, [ os.getenv('Column1'), os.getenv('Column2'), os.getenv('Column3'), os.getenv('Column4')]]

correct_column_names = sage_column_data.rename(columns={os.getenv('Column1'):os.getenv('Column_1'),os.getenv('Column2'):os.getenv('Column_2'),os.getenv('Column3'):os.getenv('Column_3'),os.getenv('Column4'):os.getenv('Column_4'),})

