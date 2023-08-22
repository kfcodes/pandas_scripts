import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv("../.env")

def process_po_data(data, po_name_data):
    try:

        po_names = po_name_data.loc[:, [ os.getenv('POINPUT1'), os.getenv('POINPUT2'), os.getenv('POINPUT3')]]
        name_table = po_names.rename(columns={os.getenv('POINPUT1'):os.getenv('POOUTPUT1'),os.getenv('POINPUT2'):os.getenv('POOUTPUT2'),os.getenv('POINPUT3'):os.getenv('POOUTPUT3'),})
        name_table.dropna();
        name_table[os.getenv('POINPUT1')].drop_duplicates().reset_index(drop=True)
        po_data = name_table;

        po_items = data.loc[:, [ os.getenv('POINPUT4'), os.getenv('POINPUT5'), os.getenv('POINPUT6'), os.getenv('POINPUT7')]]
        data_table = po_items.rename(columns={os.getenv('POINPUT4'):os.getenv('POOUTPUT4'),os.getenv('POINPUT5'):os.getenv('POOUTPUT5'),os.getenv('POINPUT6'):os.getenv('POOUTPUT6'),os.getenv('POINPUT7'):os.getenv('POOUTPUT7'),})
        data_table.dropna();
        po_item_data = data_table;

        return(po_data, po_item_data);

    except Exception as ex:
        print("Data could not be processed: \n", ex)
