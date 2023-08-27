from xlsx.read_database_file import read_xlsx_file_by_sheet
from process_data.process_label_data import process_label_data
from database.index import update_labels
import os
from dotenv import load_dotenv
load_dotenv("../.env")

data = read_xlsx_file_by_sheet('LABELSFILE', os.getenv('SHEETNAME'))
processed_data = process_label_data(data);
update_labels(processed_data);
