import os
from dotenv import load_dotenv
load_dotenv("../.env")

def create_small_label_outline():
    try:
        zpl = f"""
^XA^CFD^FWN
^FO10,68^GB795,10,7^FS
^CF0,30
^FO30,90^FD{os.getenv("LABELFIELD2")}:^FS
^FO30,130^FD{os.getenv("LABELFIELD3")}:^FS
^FO30,170^FD{os.getenv("LABELFIELD29")}:^FS
^FO30,210^FD{os.getenv("LABELFIELD28")}:^FS
^FO30,250^FD{os.getenv("LABELFIELD7")}:^FS
^FO30,290^FD{os.getenv("LABELFIELD6")}:^FS
^FO30,330^FD{os.getenv("LABELFIELD8")}:^FS
"""
        return(zpl)
    except Exception as ex:
        print("Data could not be processed: \n", ex)

def create_small_label_data(label_info, qty):
    try:
        field_9 = os.getenv("LABELFIELD9")
        field_11 = os.getenv("LABELFIELD11")
        field_12 = os.getenv("LABELFIELD12")
        field_13 = os.getenv("LABELFIELD13")
        field_14 = os.getenv("LABELFIELD14")
        field_15 = os.getenv("LABELFIELD15")
        field_16 = os.getenv("LABELFIELD16")
        field_17 = os.getenv("LABELFIELD17")
        zpl = f"""
^PQ{qty}
^CF0,40
^FO60,25^FD{label_info[field_9][0]}^FS
^CF0,30
^FO330,90 ^FD{label_info[field_11][0]}^FS
^FO330,130 ^FD{label_info[field_12][0]}^FS
^FO330,170 ^FD{label_info[field_13][0]}^FS
^FO330,210 ^FD{label_info[field_14][0]}^FS
^FO330,250 ^FD{label_info[field_15][0]}^FS
^FO330,290 ^FD{label_info[field_16][0]}^FS
^FO330,330 ^FD{label_info[field_17][0]}^FS
^XZ
"""
        return(zpl)
    except Exception as ex:
        print("Data could not be processed: \n", ex)
