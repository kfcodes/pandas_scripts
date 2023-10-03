import sys
from modules.production_info import get_component_data

id = str(sys.argv[1])

get_component_data(id);
