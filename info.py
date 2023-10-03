import sys
import os
from dotenv import load_dotenv

from modules.production_info import get_component_data

load_dotenv(".env")
id = os.getenv("ID");

id = str(sys.argv[1])

get_component_data(id);
