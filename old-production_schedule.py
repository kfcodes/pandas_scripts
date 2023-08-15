import pandas as pd
import sqlalchemy as sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import mysql.connector
import db_connection
import os
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from dotenv import load_dotenv
load_dotenv(".env")

sheets = pd.ExcelFile('schedule.xlsx')

product_database = pd.read_sql('product_database', engine, columns = ["product_description", 'product_id'])
choices = product_database.product_description.tolist()
brand_prefix = pd.read_sql('brand', engine, columns = ["prefix"], index_col="name")
brand_prefix = pd.read_sql('brand', engine)
