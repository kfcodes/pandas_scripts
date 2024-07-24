import os
from dotenv import load_dotenv
load_dotenv("../../.server_config_files/fastAPI.env")

def create_large_product_label_outline():
    try:
        zpl = f"""
^XA^CFD^FWR^LH2,5

^FO582,0^GB5,1200,2^FS
^FO520,0^GB5,1200,2^FS
^FO400,0^GB5,1200,2^FS
^FO523,520^GB60,5,2^FS
^FO400,440^GB120,5,2^FS
^FO400,840^GB120,5,2^FS

^FO530,20^A0,40^FD{os.getenv("LABELFIELD1")}:^FS
^FO531,20^A0,40^FD{os.getenv("LABELFIELD1")}:^FS
^FO532,20^A0,40^FD{os.getenv("LABELFIELD1")}:^FS
^FO530,590^A0,40^FD{os.getenv("LABELFIELD_0")}:^FS
^FO531,590^A0,40^FD{os.getenv("LABELFIELD_0")}:^FS
^FO532,590^A0,40^FD{os.getenv("LABELFIELD_0")}:^FS

^FO460,20^A0,40^FD{os.getenv("LABELFIELD_3")}^FS
^FO461,20^A0,40^FD{os.getenv("LABELFIELD_3")}^FS
^FO462,20^A0,40^FD{os.getenv("LABELFIELD_3")}^FS
^FO460,560^A0,40^FD{os.getenv("LABELFIELD6")}^FS
^FO461,560^A0,40^FD{os.getenv("LABELFIELD6")}^FS
^FO462,560^A0,40^FD{os.getenv("LABELFIELD6")}^FS
^FO460,920^A0,40^FD{os.getenv("LABELFIELD7")}^FS
^FO461,920^A0,40^FD{os.getenv("LABELFIELD7")}^FS
^FO462,920^A0,40^FD{os.getenv("LABELFIELD7")}^FS
^FO350,120^A0,40^FD{os.getenv("LABELFIELD_2")}^FS
^FO351,120^A0,40^FD{os.getenv("LABELFIELD_2")}^FS
^FO352,120^A0,40^FD{os.getenv("LABELFIELD_2")}^FS
^FO350,740^A0,40^FD{os.getenv("LABELFIELD_1")}^FS
^FO351,740^A0,40^FD{os.getenv("LABELFIELD_1")}^FS
^FO352,740^A0,40^FD{os.getenv("LABELFIELD_1")}^FS
"""
        return(zpl)
    except Exception as ex:
        print("Data could not be processed: \n", ex)

def create_large_product_label_data(label_info, qty, quantity_in_a_box, exp):
    try:

        field_9 = os.getenv("LABELFIELD9")
        field_10 = os.getenv("LABELFIELD10")
        field_11 = os.getenv("LABELFIELD11")
        field_12 = os.getenv("LABELFIELD12")
        field_14 = os.getenv("LABELFIELD14")
        field_16 = os.getenv("LABELFIELD16")
        field_15 = os.getenv("LABELFIELD15")
        field_18 = os.getenv("LABELFIELD18")
        field__18 = os.getenv("LABELFIELD__18")

        zpl = f"""
^PQ{qty},10,1,Y
^FO700,300^A0,90^FD{label_info[field_9]}^FS
^FO650,20^A@90,40,40,E:ARIALB.TTF^FD{label_info[field_11]} ({label_info[field_14]})^FS
^FO590,20^A@90,40,40,E:ARIALB.TTF^FD{label_info[field_12]}^FS
^FO530,150^A@90,40,40,E:ARIALB.TTF^FD{label_info[field_10]}^FS
^FO530,700^A@90,40,40,E:ARIALB.TTF^FD{label_info[field_18]}^FS
^FO410,170^A@90,40,40,E:ARIALB.TTF^FD{quantity_in_a_box}^FS
^FO410,520^A@90,40,40,E:ARIALB.TTF^FD{label_info[field_15]}^FS
^FO410,880^A@90,40,40,E:ARIALB.TTF^FD{label_info[field_16]}^FS
^BY2,2.5,200
^FO70,100
^BCR,,N,N,N,A
^FD>:>8010{label_info[field__18]}>810{label_info[field_15]}>815{exp}^FS
^FT35,240
^A0R,30,30
^FD(01)0{label_info[field__18]}(10){label_info[field_15]}(15){exp}^FS
^XZ
"""
        return(zpl)
    except Exception as ex:
        print("Data could not be processed: \n", ex)
                # ^FD>;>801{label_info[field__18]}>810>6{label_info[field_17]}>815>8260218^FS
                # ^FD(01){label_info[field__18]}(10){label_info[field_17]}(15)260218^FS
