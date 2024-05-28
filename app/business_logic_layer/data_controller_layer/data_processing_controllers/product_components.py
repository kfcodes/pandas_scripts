from business_logic_layer.external_module_controllers.excel_file_logic.read_xlsx_file import read_data
from business_logic_layer.external_module_controllers.data_analysis_logic.process_component_data import process_component_data
from physical_layer.data_access_layer.write_database_functions import update_components

def process_components_file():
    try:
        data = read_data('COMPONENTSFILE')
        processed_data = process_component_data(data);
        update_components(processed_data);

    except Exception as ex:
        print("Data could not be processed: \n", ex)
