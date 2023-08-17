import pandas as pd
import sqlalchemy as sqlalchemy
import os
from dotenv import load_dotenv
load_dotenv("../../.env")

dataframe = pd.read_excel(os.getenv('DATABASE_FILE'))

database_data = dataframe.loc[:, [ os.getenv('Column1'), os.getenv('Column2'), os.getenv('Column3'), os.getenv('Column4')]]
new_data = database_data.rename(columns={os.getenv('Column1'):os.getenv('Column_1'),os.getenv('Column2'):os.getenv('Column_2'),os.getenv('Column3'):os.getenv('Column_3'),os.getenv('Column4'):os.getenv('Column_4'),})

print(new_data);

