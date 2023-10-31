import xmltodict
import os
from dotenv import load_dotenv
load_dotenv(".env")

bom = os.getenv('XML')

# The output is formatted to be more readable for the end user

with open(b) as fd:
    xml_dict = xmltodict.parse(fd.read(), process_namespaces=True)
    for product in xml_dict['BOMRecords']['BOMRecord']:
        product_code = product['Reference']
        product_description = product['Description']
        # print( product_code + ' - ' + product_description )
        print("================================================================================================")
        print(product_code + " " + product_description)


