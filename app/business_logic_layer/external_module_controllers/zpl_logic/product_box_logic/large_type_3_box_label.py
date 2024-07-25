import os
from dotenv import load_dotenv
load_dotenv("../.env")

def create_large_product_label_outline():
    try:
        zpl = f"""
^XA^CFD^FWR^LH2,5
^FO750,30^A0,40^FDGTIN:^FS
^FO751,30^A0,40^FDGTIN:^FS
^FO752,30^A0,40^FDGTIN:^FS
^FO620,30^A0,40^FDLOT:^FS
^FO621,30^A0,40^FDLOT:^FS
^FO622,30^A0,40^FDLOT:^FS
^FO570,30^A0,40^FDBBE:^FS
^FO571,30^A0,40^FDBBE:^FS
^FO572,30^A0,40^FDBBE:^FS
^FO520,30^A0,40^FDQTY:^FS
^FO521,30^A0,40^FDQTY:^FS
^FO522,30^A0,40^FDQTY:^FS
^FO470,30^A0,40^FDREF:^FS
^FO471,30^A0,40^FDREF:^FS
^FO472,30^A0,40^FDREF:^FS
"""
        return(zpl)
    except Exception as ex:
        print("data could not be processed: \n", ex)

def create_large_product_label_data(label_info, qty, quantity_in_a_box, exp):
    print(label_info)
    try:
        field_18 = os.getenv("LABELFIELD18")
        field_15 = os.getenv("LABELFIELD15")
        field_16 = os.getenv("LABELFIELD16")
        field_10 = os.getenv("LABELFIELD10")
        field_11 = os.getenv("LABELFIELD11")
        zpl = f"""
^PQ{qty},10,1,Y
^FO750,200^A0,40^FD{label_info[field_18]}^FS
^FO680,60^A0,50^FD{label_info[field_11]}^FS
^FO620,200^A0,40^FD{label_info[field_15]}^FS
^FO570,200^A0,40^FD{label_info[field_16]}^FS
^FO520,200^A0,40^FD{quantity_in_a_box}^FS
^FO470,200^A0,40^FD{label_info[field_10]}^FS
^BY3,2,180
^FO280,100
^BCR,,N,N,N,A
^FD>:>801{label_info[field_18]}>810{label_info[field_15]}^FS 
^FT250,320
^A0R,30,30
^FD(01) {label_info[field_18]} (10) {label_info[field_15]}^FS
^FO50,100
^BCR,,N,N,N,A
^FD>;>815{exp}>8300000000{quantity_in_a_box}^FS 
^FT20,200
^A0R,30,30
^FD(15) {exp} (30) 0000000{quantity_in_a_box}^FS
^XZ
"""
        return(zpl)
    except Exception as ex:
        print("data could not be processed: \n", ex)
