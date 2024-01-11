import os
from dotenv import load_dotenv
load_dotenv("../../.env")

def create_large_product_label_outline():
    try:
        zpl = f"""
                ^XA^CFD^FWR^LH2,20
                ^FO650,20^A0,50^A@90,50,50,E:ARIALBLB.TTF^FD{os.getenv("LABELFIELD1")}:^FS
                ^FO600,20^A@90,50,50,E:ARIALBLB.TTF^FD{os.getenv("LABELFIELD2")}:^FS
                ^FO550,20^A@90,50,50,E:ARIALBLB.TTF^FD{os.getenv("LABELFIELD3")}:^FS
                ^FO500,20^A@90,50,50,E:ARIALBLB.TTF^FD{os.getenv("LABELFIELD4")}:^FS
                ^FO450,20^A@90,50,50,E:ARIALBLB.TTF^FD{os.getenv("LABELFIELD5")}:^FS
                ^FO400,20^A@90,50,50,E:ARIALBLB.TTF^FD{os.getenv("LABELFIELD6")}:^FS
                ^FO350,20^A@90,50,50,E:ARIALBLB.TTF^FD{os.getenv("LABELFIELD7")}:^FS
                ^FO300,20^A@90,50,50,E:ARIALBLB.TTF^FD{os.getenv("LABELFIELD8")}:^FS
            """
        return(zpl)
    except Exception as ex:
        print("Data could not be processed: \n", ex)

def create_large_product_label_data(label_info, qty):
    try:
        field_9 = os.getenv("LABELFIELD9")
        field_10 = os.getenv("LABELFIELD10")
        field_11 = os.getenv("LABELFIELD11")
        field_12 = os.getenv("LABELFIELD12")
        field_13 = os.getenv("LABELFIELD13")
        field_14 = os.getenv("LABELFIELD14")
        field_15 = os.getenv("LABELFIELD15")
        field_16 = os.getenv("LABELFIELD16")
        field_17 = os.getenv("LABELFIELD17")
        field_18 = os.getenv("LABELFIELD18")
        zpl = f"""
                ^PQ{qty},10,1,Y
                ^FO700,250^A0,90^FD{label_info[field_9]}^FS
                ^FO650,450^A@90,50,50,E:ARIALB.TTF^FD{label_info[field_10]}^FS
                ^FO600,450^A@90,50,50,E:ARIALB.TTF^FD{label_info[field_11]}^FS
                ^FO550,450^A@90,50,50,E:ARIALB.TTF^FD{label_info[field_12]}^FS
                ^FO500,450^A@90,50,50,E:ARIALB.TTF^FD{label_info[field_13]}^FS
                ^FO450,450^A@90,50,50,E:ARIALB.TTF^FD{label_info[field_14]}^FS
                ^FO400,450^A@90,50,50,E:ARIALB.TTF^FD{label_info[field_15]}^FS
                ^FO350,450^A@90,50,50,E:ARIALB.TTF^FD{label_info[field_16]}^FS
                ^FO300,450^A@90,50,50,E:ARIALB.TTF^FD{label_info[field_17]}^FS
                ^BY8^FO70,200^BER,210,Y,N,N,N,N^FD{label_info[field_18]}^FS ^XZ
            """
        return(zpl)
    except Exception as ex:
        print("Data could not be processed: \n", ex)
