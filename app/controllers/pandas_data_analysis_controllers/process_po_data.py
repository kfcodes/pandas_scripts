import os
from dotenv import load_dotenv
load_dotenv("../../../.env")

def process_po_data(data, po_name_data):

    try:

        po_names = po_name_data.loc[:, [ os.getenv('POINPUT1'), os.getenv('POINPUT2'), os.getenv('POINPUT3'), os.getenv('POINPUT4')]]

        po_names = po_names[~po_names[os.getenv('POINPUT4')].str.contains(os.getenv('PODELETE5'))]
        po_names.drop(columns=[os.getenv('POINPUT4')])
        po_names = po_names[~po_names[os.getenv('POINPUT1')].str.contains(os.getenv('PODELETE2'))]
        po_names = po_names[~po_names[os.getenv('POINPUT1')].str.contains(os.getenv('PODELETE3'))]

        name_table = po_names.rename(columns={os.getenv('POINPUT1'):os.getenv('POOUTPUT1'),os.getenv('POINPUT2'):os.getenv('POOUTPUT2'),os.getenv('POINPUT3'):os.getenv('POOUTPUT3'),})
        name_table.dropna();
        name_table[os.getenv('POOUTPUT1')].drop_duplicates().reset_index(drop=True)

        po_data = name_table[[ os.getenv('POOUTPUT1'), os.getenv('POOUTPUT2'), os.getenv('POOUTPUT3') ]]

        po = data.loc[:, [ os.getenv('POINPUT5'), os.getenv('POINPUT6'), os.getenv('POINPUT7'), os.getenv('POINPUT8')]]

        po.dropna();
        # po.dropna(subset=[os.getenv('POINPUT6')]);
        po = po[~po[os.getenv('POINPUT8')].str.contains(os.getenv('PODELETE5'))]
        po = po[~po[os.getenv('POINPUT5')].str.contains(os.getenv('PODELETE2'))]
        po = po[~po[os.getenv('POINPUT5')].str.contains(os.getenv('PODELETE3'))]
        po = po[~po[os.getenv('POINPUT6')].str.contains(os.getenv('PODELETE4'), na=True)]

        po_details = po.loc[:, [ os.getenv('POINPUT5'), os.getenv('POINPUT6'), os.getenv('POINPUT7')]]
        data_table = po_details.rename(columns={os.getenv('POINPUT5'):os.getenv('POOUTPUT5'), os.getenv('POINPUT6'):os.getenv('POOUTPUT6'), os.getenv('POINPUT7'):os.getenv('POOUTPUT7'),})
        
        po_item_data = data_table;
        
        return(po_data, po_item_data);
        
    except Exception as ex:
        print("Data could not be processed: \n", ex)
