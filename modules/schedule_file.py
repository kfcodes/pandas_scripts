from xlsx.read_xlsx_file import read_xlsx_file_skip_first_row
from process_data.process_schedule_data import process_schedule_data
from database.write_db_index import update_schedule

data= read_xlsx_file_skip_first_row('SCHEDULEFILE')
processed_data = process_schedule_data(data);
print(processed_data);
# update_schedule(processed_data);
