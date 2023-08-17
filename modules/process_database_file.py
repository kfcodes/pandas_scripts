# from dotenv import load_dotenv
# load_dotenv("../.env")
# import sqlalchemy as sqlalchemy
# from database.write import write_to_database
from xlsx.read_database_file import read_xlsx_file
from process_data.process_database_data import process_data
from database.index import updateDB

dataframe = read_xlsx_file('DATABASE_FILE')
new_data = process_data(dataframe);
# write_to_database(new_data, 'tpdb_table')
updateDB(new_data);
