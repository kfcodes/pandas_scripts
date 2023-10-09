import os
from dotenv import load_dotenv

from modules.database.read_db_index import get_label_info

from modules.zpl.create_production_label_zpl import create_label_outline, add_info_to_label

# from modules.print.print_pdf import print_a4_pdf

load_dotenv(".env")

def get_label_data(id):
    try:
        
        label_info = get_label_info(f"{os.getenv('PRODUCTIONLABELINFO')}{id}")

        # write the label outline to the file
        label_outline = create_label_outline(label_info)

        # write the label data to the file
        label_outline_and_data = add_info_to_label(label_info)

        # print_zpl_file(label_file)

    except Exception as ex:
        print("Data could not be processed: \n", ex)
