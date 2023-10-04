import os
from dotenv import load_dotenv
from controllers.db_file import process_db_file
from controllers.components_file import process_components_file
from controllers.label_file import process_label_file
from controllers.po_file import process_po_files
from controllers.schedule_file import process_schedule_file

load_dotenv(".env")
sheet = os.getenv("SHEETINPUT");

process_db_file()
process_components_file();
process_label_file();
process_po_files();
process_schedule_file(sheet);
