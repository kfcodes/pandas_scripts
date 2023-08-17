from xlsx.read_database_file import read_xlsx_file
from process_data.process_database_data import process_data
from database.index import updateDB

dataframe = read_xlsx_file('DATABASE_FILE')
new_data = process_data(dataframe);
updateDB(new_data);
