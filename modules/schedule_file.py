from modules.xlsx.read_xlsx_file import read_xlsx_file_sheet_skip_first_row
from modules.process_data.process_schedule_data import process_schedule_data
from modules.database.write_db_index import update_schedule

def process_schedule_file(sheet):
    try:
        data= read_xlsx_file_sheet_skip_first_row('SCHEDULEFILE', sheet)
        processed_data = process_schedule_data(data);
        update_schedule(processed_data);
    except Exception as ex:
        print("Data could not be processed: \n", ex)
