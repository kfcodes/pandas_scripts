from xlsx.read_database_file import read_xlsx_file
from process_data.process_label_data import process_label_data
from database.index import update_labels

data = read_xlsx_file('LABELSFILE')
processed_data = process_label_data(data);
update_labels(processed_data);
