from app.controllers.data_processing_controllers.db_file import process_db_file
from app.controllers.data_processing_controllers.components_file import process_components_file
from app.controllers.data_processing_controllers.label_file import process_label_file
from app.controllers.data_processing_controllers.po_file import process_po_files
from app.controllers.data_processing_controllers.schedule_file import process_schedule_file

import os
from dotenv import load_dotenv
load_dotenv(".env")
sheet = os.getenv("SHEETINPUT");

process_db_file()
process_components_file();
process_label_file();
process_po_files();
process_schedule_file(sheet);
