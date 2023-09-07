from xlsx.read_xlsx_file import read_full_xlsx_file
from process_data.process_component_data import process_component_data
from database.write_db_index import update_components

data = read_full_xlsx_file('COMPONENTSFILE')
processed_data = process_component_data(data);
update_components(processed_data);
