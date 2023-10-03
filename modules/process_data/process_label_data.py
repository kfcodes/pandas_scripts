import os
from dotenv import load_dotenv
load_dotenv(".env")

def process_label_data(data):
    try:

        label_data = data.loc[:, [ os.getenv('LABELINPUT1'), os.getenv('LABELINPUT2'), os.getenv('LABELINPUT3'), os.getenv('LABELINPUT4'), os.getenv('LABELINPUT5'), os.getenv('LABELINPUT6'), os.getenv('LABELINPUT7'), os.getenv('LABELINPUT8')]]

        label_dataa = label_data[label_data[os.getenv('LABELINPUT8')].notna()]

        processed_data = label_dataa.rename(columns={os.getenv('LABELINPUT1'):os.getenv('LABELOUTPUT1'),os.getenv('LABELINPUT2'):os.getenv('LABELOUTPUT2'),os.getenv('LABELINPUT3'):os.getenv('LABELOUTPUT3'),os.getenv('LABELINPUT4'):os.getenv('LABELOUTPUT4'),os.getenv('LABELINPUT5'):os.getenv('LABELOUTPUT5'),os.getenv('LABELINPUT6'):os.getenv('LABELOUTPUT6'),os.getenv('LABELINPUT7'):os.getenv('LABELOUTPUT7'),os.getenv('LABELINPUT8'):os.getenv('LABELOUTPUT8'),})

        return(processed_data)

    except Exception as ex:

        print("Data could not be processed: \n", ex)
