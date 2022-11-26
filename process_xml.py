import xmltodict

with open('../test.xml') as fd:
    xml_dict = xmltodict.parse(fd.read(), process_namespaces=True)
    print(xml_dict)
