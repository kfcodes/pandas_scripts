from xlsx.read_xlsx_file import read_full_xlsx_file
from process_data.process_database_data import process_db_data
from database.write_db_index import update_db

data= read_full_xlsx_file('DBFILE')
processed_data = process_db_data(data);
update_db(processed_data);
