import xmltodict
import os
from dotenv import load_dotenv
load_dotenv(".env")

bom = os.getenv('XML')

# The loop new extracts the components from the xml file
with open(product) as fd:
    xml_dict = xmltodict.parse(fd.read(), process_namespaces=True)
    for producti in xml_dict['Record']
        product_code = product['Reference']
        product_description = product['Description']
        # print( product_code + ' - ' + product_description )
            print(product)
