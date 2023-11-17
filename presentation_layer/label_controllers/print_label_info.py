# from ...data_access_layer.read_database_functions import get_label_data
# from ...business_logic_layer.zpl_controllers.create_small_label import create_small_label_data,  create_small_label_outline
from business_logic_layer.zpl_controllers.create_small_label import create_small_label_data,  create_small_label_outline
from business_logic_layer.print_controllers.print_zpl import print_small_label

import os
from dotenv import load_dotenv
load_dotenv("../.env")

def print_small_label_with_data():

    try:
        
        # label_info = get_label_data(f"{os.getenv('PRODUCTIONLABELINFO')}{id}")
        label_info = "test"

        outline = create_small_label_outline()
        body = create_small_label_data(label_info)
    
        label_data = outline + body

        print_small_label(label_data)

    except Exception as ex:
        print("Data could not be processed: \n", ex)
