import xmltodict
import os
from dotenv import load_dotenv
load_dotenv(".env")

bom = os.getenv('XML')

# The loop new extracts the components from the xml file
with open(p) as fd:
    xml_dict = xmltodict.parse(fd.read(), process_namespaces=True)
    for product in xml_dict['BOMRecords']['BOMRecord']:
        product_code = product['Reference']
        product_description = product['Description']
        print( product_code + ' - ' + product_description )
