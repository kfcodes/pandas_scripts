from xlsx.read_database_file import read_xlsx_file
from process_data.process_database_data import process_data
from database.index import updateDB

data= read_xlsx_file('DATABASE_FILE')
formatted_data = process_data(data);
updateDB(formatted_data);
