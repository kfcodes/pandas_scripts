import os
from dotenv import load_dotenv
load_dotenv("../../.env")

def create_large_product_label_outline():
    try:
        zpl_outline = f"""^XA^CFD^FWR^LH30,10
^FO650,50^A0,50^FDOrdered by:^FS
^FO550,50^A0,50^FDProduct Name:^FS
^FO450,50^A0,50^FDNet Weight:^FS^FO450,460^A0,50^FDkg^FS
^FO350,50^A0,50^FDMfg. Date:^FS
^FO250,50^A0,50^FDBBE:^FS
^FO150,50^A0,50^FDBatch No:^FS
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
^FO550,400^A0,50^FD{label_info[field_11]}^FS
^FO450,400^A0,50^FD{quantity_in_a_box}^FS
^FO350,400^A0,50^FD{exp}^FS
^FO250,400^A0,50^FD{label_info[field_16]}^FS
^FO150,400^A0,50^FD{label_info[field_15]}^FS
^XZ"""
        return(zpl)
    except Exception as ex:
        print("data could not be processed: \n", ex)
