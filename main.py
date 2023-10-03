from modules.db_file import process_db_file
from modules.components_file import process_components_file
from modules.label_file import process_label_file
from modules.po_file import process_po_files
from modules.schedule_file import process_schedule_file

sheet = "test"

process_db_file()
process_components_file();
process_label_file();
process_po_files();
process_schedule_file(sheet);
