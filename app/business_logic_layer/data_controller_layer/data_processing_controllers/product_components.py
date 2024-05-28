from business_logic_layer.xlsx_logic_module.read_xlsx_file import read_data
from business_logic_layer.pandas_logic_module.process_component_data import process_component_data
from data_access_layer.write_database_functions import update_components

def process_components_file():
    try:
        data = read_data('COMPONENTSFILE')
        processed_data = process_component_data(data);
        update_components(processed_data);

    except Exception as ex:
        print("Data could not be processed: \n", ex)
