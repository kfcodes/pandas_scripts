import sys
from .business_logic_layer.production_documentation_controllers import get_component_data

id = str(sys.argv[1])
get_component_data(id);
