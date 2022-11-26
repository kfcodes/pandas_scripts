import xmltodict

with open('../test.xml') as fd:
    xml_dict = xmltodict.parse(fd.read(), process_namespaces=True)
    for product in xml_dict['BOMRecords']['BOMRecord']:
        print(product)
