from xlsx.read_database_file import read_xlsx_file
from process_data.process_database_data import process_data
from database.index import update_db

data= read_xlsx_file('DATABASE_FILE')
formatted_data = process_data(data);
update_db(formatted_data);
