from xlsx.read_database_file import read_xlsx_file
from process_data.process_components_data import process_components_data
from database.index import update_components

data = read_xlsx_file('COMPONENTSFILE')
processed_data = process_components_data(data);
update_components(processed_data);
