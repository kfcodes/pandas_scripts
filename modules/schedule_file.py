from xlsx.read_database_file import read_xlsx_file
from process_data.process_schedule_data import process_schedule_data
from database.write_db_index import update_schedule

data= read_xlsx_file('SCHEDULEFILE')
processed_data = process_schedule_data(data);
update_schedule(processed_data);
