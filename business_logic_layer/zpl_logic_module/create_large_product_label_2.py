import os
from dotenv import load_dotenv
load_dotenv("../../.env")

def create_large_product_label_outline():
    try:
        zpl = f"""
                ^XA^CFD^FWR^LH2,20

                ^FO650,20^A0,50^FD{os.getenv("LABELFIELD2")}:^FS
                ^FO651,20^A0,50^FD{os.getenv("LABELFIELD2")}:^FS
                ^FO652,20^A0,50^FD{os.getenv("LABELFIELD2")}:^FS

                ^FO600,20^A0,50^FD{os.getenv("LABELFIELD3")}:^FS
                ^FO601,20^A0,50^FD{os.getenv("LABELFIELD3")}:^FS
                ^FO602,20^A0,50^FD{os.getenv("LABELFIELD3")}:^FS

                ^FO550,20^A0,50^FD{os.getenv("LABELFIELD1")}:^FS
                ^FO551,20^A0,50^FD{os.getenv("LABELFIELD1")}:^FS
                ^FO552,20^A0,50^FD{os.getenv("LABELFIELD1")}:^FS

                ^FO500,20^A0,50^FD{os.getenv("LABELFIELD_0")}:^FS
                ^FO501,20^A0,50^FD{os.getenv("LABELFIELD_0")}:^FS
                ^FO502,20^A0,50^FD{os.getenv("LABELFIELD_0")}:^FS

                ^FO450,20^A0,50^FD{os.getenv("LABELFIELD_3")}:^FS
                ^FO451,20^A0,50^FD{os.getenv("LABELFIELD_3")}:^FS
                ^FO452,20^A0,50^FD{os.getenv("LABELFIELD_3")}:^FS

                ^FO400,20^A0,50^FD{os.getenv("LABELFIELD_1")}:^FS
                ^FO401,20^A0,50^FD{os.getenv("LABELFIELD_1")}:^FS
                ^FO402,20^A0,50^FD{os.getenv("LABELFIELD_1")}:^FS

                ^FO350,20^A0,50^FD{os.getenv("LABELFIELD_2")}:^FS
                ^FO351,20^A0,50^FD{os.getenv("LABELFIELD_2")}:^FS
                ^FO352,20^A0,50^FD{os.getenv("LABELFIELD_2")}:^FS

                ^FO300,20^A0,50^FD{os.getenv("LABELFIELD6")}:^FS
                ^FO301,20^A0,50^FD{os.getenv("LABELFIELD6")}:^FS
                ^FO302,20^A0,50^FD{os.getenv("LABELFIELD6")}:^FS

                ^FO250,20^A0,50^FD{os.getenv("LABELFIELD7")}:^FS
                ^FO251,20^A0,50^FD{os.getenv("LABELFIELD7")}:^FS
                ^FO252,20^A0,50^FD{os.getenv("LABELFIELD7")}:^FS
            """
        return(zpl)
    except Exception as ex:
        print("Data could not be processed: \n", ex)

def create_large_product_label_data(label_info, qty, quantity_in_a_box):
    try:

        field_9 = os.getenv("LABELFIELD9")
        field_10 = os.getenv("LABELFIELD10")
        field_11 = os.getenv("LABELFIELD11")
        field_12 = os.getenv("LABELFIELD12")
        field_16 = os.getenv("LABELFIELD16")
        field_17 = os.getenv("LABELFIELD17")
        field_18 = os.getenv("LABELFIELD18")
        field__18 = os.getenv("LABELFIELD__18")

        zpl = f"""
                ^PQ{qty},10,1,Y

                ^FO700,300^A0,90^FD{label_info[field_9]}^FS

                ^FO650,450^A@90,50,50,E:ARIALB.TTF^FD{label_info[field_11]}^FS
                ^FO600,450^A@90,50,50,E:ARIALB.TTF^FD{label_info[field_12]}^FS
                ^FO550,450^A@90,50,50,E:ARIALB.TTF^FD{label_info[field_10]}^FS
                ^FO500,450^A@90,50,50,E:ARIALB.TTF^FD{label_info[field_18]}^FS
                ^FO450,550^A@90,50,50,E:ARIALB.TTF^FD{quantity_in_a_box}^FS
                ^FO300,550^A@90,50,50,E:ARIALB.TTF^FD{label_info[field_17]}^FS
                ^FO250,550^A@90,50,50,E:ARIALB.TTF^FD{label_info[field_16]}^FS

                ^BY5,2.5,170
                ^FO70,300
                ^BCR,,N,N,N,A
                ^FD>;>801{label_info[field__18]}^FS

                ^FT35,420
                ^ABR,20,20
                ^FD(01){label_info[field__18]}^FS
                ^XZ
            """
        return(zpl)
    except Exception as ex:
        print("Data could not be processed: \n", ex)
