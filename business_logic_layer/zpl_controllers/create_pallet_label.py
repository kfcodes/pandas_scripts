import os
from dotenv import load_dotenv
load_dotenv("../../.env")

def create_pallet_label_outline():
    try:
        zpl = """
                ^XA^CFD^FWR^LH2,10^PQ2
                ^FO600,0^GB5,1200,5^FS
                ^FO450,0^GB5,1200,5^FS
                ^FO450,800^GB150,5,5^FS
                ^FO10,800^GB200,5,5^FS
                ^FO210,400^GB390,5,5^FS
                ^FO210,0^GB5,1900,5^FS
                ^FO150,890^A0,40^FDCHECKED BY:^FS
                 ^FO490,1100^A0,60^FD(KG)^FS
            """
        return(zpl)
    except Exception as ex:
        print("Data could not be processed: \n", ex)

def create_pallet_label_data_part_1(label_info):
    try:
        pallet_label_field_1 = os.getenv("PALLETLABEL1")
        pallet_label_field_2 = os.getenv("PALLETLABEL2")
        pallet_label_field_3 = os.getenv("PALLETLABEL3")
        pallet_label_field_4 = os.getenv("PALLETLABEL4")
        pallet_label_field_5 = os.getenv("PALLETLABEL5")
        zpl = f"""
                ^FO660,250^BY5 ^BC90,120,Y,N,N^FD{label_info[pallet_label_field_1][0]}^FS
                ^FO60,150^A0,80^FD^FS^FD{label_info[pallet_label_field_2][0]}^FS
                ^FO490,20^A0,60^FD^FS^FD{label_info[pallet_label_field_3][0]}^FS
                ^FO490,450^A0,60^FD^FS^FD{label_info[pallet_label_field_4][0]}^FS
                ^FO490,900^A0,60^FD^FS^FD{label_info[pallet_label_field_5][0]}^FS
                ^XZ
                """
        return(zpl)
    except Exception as ex:
        print("Data could not be processed: \n", ex)
