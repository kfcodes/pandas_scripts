from ..xlsx_controllers.read_xlsx_file import read_data
from ..pandas_data_analysis_controllers.process_component_data import process_component_data
from ..database_controllers.write_db_index import update_components

def process_components_file():

    try:

        data = read_data('COMPONENTSFILE')
        processed_data = process_component_data(data);
        update_components(processed_data);

    except Exception as ex:
        print("Data could not be processed: \n", ex)
