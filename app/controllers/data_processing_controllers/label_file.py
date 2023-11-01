from app.modules.xlsx.read_xlsx_file import read_xlsx_file_by_sheet
from app.modules.process_data.process_label_data import process_label_data
from app.modules.database.write_db_index import update_labels
import os
from dotenv import load_dotenv
load_dotenv(".env")

def process_label_file():
    try:
        data = read_xlsx_file_by_sheet('LABELSFILE', os.getenv('SHEETNAME'))
        processed_data = process_label_data(data);
        update_labels(processed_data);
    except Exception as ex:
        print("Data could not be processed: \n", ex)
