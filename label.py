import sys
from app.controllers.print_label_info import print_label_with_data

id = str(sys.argv[1])
print_label_with_data(id);
