# Pandas now processes the components into one line table that can be inserted into db
import sys
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

def get_component(row):
    if row['Type'] == 'Component':
        component_name = row['Name']
        lowercase_component_name = component_name.lower()
        if os.getenv('COMPONENT_DESCRIPTION1') in lowercase_component_name:
            return os.getenv('TYPE1')
        if os.getenv('COMPONENT_DESCRIPTION2') in lowercase_component_name:
            return os.getenv('TYPE2')
        if os.getenv('COMPONENT_DESCRIPTION3') in lowercase_component_name:
            return os.getenv('TYPE3')
        if os.getenv('COMPONENT_DESCRIPTION4') in lowercase_component_name:
            return os.getenv('TYPE4')
        if os.getenv('COMPONENT_DESCRIPTION5') in lowercase_component_name:
            return os.getenv('TYPE5')
        if os.getenv('COMPONENT_DESCRIPTION6') in lowercase_component_name:
            return os.getenv('TYPE6')
        if os.getenv('COMPONENT_DESCRIPTION7') in lowercase_component_name:
            return os.getenv('TYPE7')
        if os.getenv('COMPONENT_DESCRIPTION8') in lowercase_component_name:
            return os.getenv('TYPE8')
        if os.getenv('COMPONENT_DESCRIPTION9') in lowercase_component_name:
            return os.getenv('TYPE9')
        if os.getenv('COMPONENT_DESCRIPTION10') in lowercase_component_name:
            return os.getenv('TYPE10')

def insert_into_db(product):
    try:
    # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        engine = db_connection.create_connection()
        product.to_sql('product', engine, if_exists='append', index=False)
        print('inserted')
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

for root, directories, filea in os.walk(path):
    for file in filea:
        if file.endswith(".xlsx"):
            file_name, file_name_extension = os.path.splitext(file)
            df = pd.read_excel(os.path.join(root,file))
            bom_name_row = df.loc[df.Type == 'Bill of Materials'].values[0]
            bom_name = bom_name_row.tolist()[0]
            subassembly_row = df.loc[df.Type == 'Subassembly'].values[0]
            subassembly_quantity = subassembly_row.tolist()[2]
            subassembly_code = subassembly_row.tolist()[0]
            df['Component Type'] = df.apply(get_component,axis=1)
            components = df.loc[:, ['Component Type', 'Code', 'Quantity']]
            d = components.dropna()
            p = d.set_index('Component Type')
            df1=p.stack().swaplevel()
            ndf = df1.to_frame().T
            ndf.columns = ndf.columns.map('{0[1]}_{0[0]}'.format)
            ndf['Subassembly_Code'] = subassembly_code
            ndf['Subassembly_Quantity'] = subassembly_quantity
            ndf['product_id'] = bom_name
            ndf= ndf.rename(columns=str.lower)
            # product = ndf.columns.str.lower()
            # ndf.columns.str.lower()
            # print(ndf)
            insert_into_db(ndf)
