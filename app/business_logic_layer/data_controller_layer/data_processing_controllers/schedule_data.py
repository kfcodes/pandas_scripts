from business_logic_layer.external_module_controllers.excel_file_logic.read_xlsx_file import read_data_after_first_row
from business_logic_layer.external_module_controllers.data_analysis_logic.process_schedule_data import process_schedule_data
from physical_layer.data_access_layer.write_database_functions import update_schedule

def process_schedule_file(sheet):
    try:
        data= read_data_after_first_row('SCHEDULEFILE', sheet)
        processed_data = process_schedule_data(data);
        update_schedule(processed_data);
         
    except Exception as ex:
        print("Data could not be processed: \n", ex)
