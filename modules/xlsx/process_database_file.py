import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv("../../.env")

database_output_file = os.getenv('DATABASE_FILE')
dataframe = pd.read_excel(database_output_file)

