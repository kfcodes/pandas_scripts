import pandas as pd
import sqlalchemy as sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import mysql.connector
# Create Database Connection
creds = {'usr': 'root',
        'pwd': 'test',
        'hst': '127.0.0.1',
        'prt': 3306,
        'dbn': 'test'}
connstr = 'mysql+mysqlconnector://{usr}:{pwd}@{hst}:{prt}/{dbn}'
engine = create_engine()

