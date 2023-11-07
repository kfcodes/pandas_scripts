from presentation_layer.data_processing_controllers.database_data import process_db_file
from presentation_layer.data_processing_controllers.label_data import process_label_file
# from presentation_layer.data_processing_controllers.product_components import process_components_file
# from presentation_layer.data_processing_controllers.po_data import process_po_files
# from presentation_layer.data_processing_controllers.schedule_data import process_schedule_file

import os
from dotenv import load_dotenv
load_dotenv(".env")

sheet = os.getenv("SHEETINPUT");

process_db_file()
# process_components_file();
process_label_file();
# process_po_files();
# process_schedule_file(sheet);
