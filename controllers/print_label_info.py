import os
from dotenv import load_dotenv
from modules.database.read_db_index import get_label_data
from modules.zpl.create_production_label import create_production_label_file

# from modules.print.print_pdf import print_a4_pdf

load_dotenv(".env")

def print_label_with_data(id):
    try:
        
        label_info = get_label_data(f"{os.getenv('PRODUCTIONLABELINFO')}{id}")

        # write the label data to the file
        label_file = create_production_label_file(label_info)
        print(label_file)

        # print_zpl_file(label_file)

    except Exception as ex:
        print("Data could not be processed: \n", ex)
