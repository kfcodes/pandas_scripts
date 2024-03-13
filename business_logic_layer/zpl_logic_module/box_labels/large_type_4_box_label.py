import os
from dotenv import load_dotenv
load_dotenv("../../.env")

def create_large_product_label_outline():
    try:
        zpl_outline = f"""^XA^CFD^FWR^LH2,5
^FO625,20^GB5,1160,2^FS
^FO100,20^GB5,1160,2^FS
^FO550,50^A0,33^FDOrdered by:^FS
^FO480,50^A0,33^FDProduct Name:^FS
^FO410,50^A0,33^FDNet Weight:^FS^FO410,340^A0,33^FDKG^FS
^FO340,50^A0,33^FDBBE:^FS
^FO270,50^A0,33^FDLOT:^FS
^FO200,50^A0,33^FDMfg. Date:^FS
^FO130,50^A0,33^FDMade in:^FS
^FO40,50^A0,33^FDWeb site:^FS
"""
        data = str(os.getenv("LABELFIELDOUTLINE"))
        zpl = zpl_outline + data
        return(zpl)
    except Exception as ex:
        print("data could not be processed: \n", ex)

def create_large_product_label_data(label_info, qty, quantity_in_a_box, exp):
    try:
        field_15 = os.getenv("LABELFIELD15")
        field_16 = os.getenv("LABELFIELD16")
        field_11 = os.getenv("LABELFIELD11")
        zpl = f"""^PQ{qty},10,1,Y
^FO480,300^A0,33^FD{label_info[field_11]}^FS
^FO410,300^A0,33^FD{quantity_in_a_box}^FS
^FO340,300^A0,33^FD{label_info[field_16]}^FS
^FO270,300^A0,33^FD{label_info[field_15]}^FS
^FO200,300^A0,33^FD{exp}^FS
^XZ"""
        return(zpl)
    except Exception as ex:
        print("data could not be processed: \n", ex)
