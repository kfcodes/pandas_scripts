from ..database_controllers.read_db_index import get_label_data
from ..zpl_controllers.create_label import create_label

import os
from dotenv import load_dotenv
load_dotenv("../../../.env")

def print_label_with_data(id):
    try:
        
        label_info = get_label_data(f"{os.getenv('PRODUCTIONLABELINFO')}{id}")

        # write the label data to the file
        label_file = create_label(label_info)

        print(label_file)

        # print_zpl_file(label_file)

    except Exception as ex:
        print("Data could not be processed: \n", ex)
