from app.modules.xlsx.read_xlsx_file import read_full_xlsx_file
from app.modules.process_data.process_component_data import process_component_data
from app.modules.database.write_db_index import update_components

def process_components_file():
    try:
        data = read_full_xlsx_file('COMPONENTSFILE')
        processed_data = process_component_data(data);
        update_components(processed_data);
    except Exception as ex:
        print("Data could not be processed: \n", ex)
