import os
from dotenv import load_dotenv
load_dotenv(".env")

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

def create_pallet_label_data(label_info):
    print(label_info)
    try:
        pallet_label_field_1 = os.getenv("PALLETLABEL1")
        pallet_label_field_2 = os.getenv("PALLETLABEL2")
        pallet_label_field_3 = os.getenv("PALLETLABEL3")
        field_3 = (label_info[f"{pallet_label_field_3}"])
        pallet_label_field_4 = os.getenv("PALLETLABEL4")
        zpl = f"""
                ^FO660,250^BY5^BC90,120,Y,N,N^FD{label_info[f"{pallet_label_field_1}"]}^FS
                ^FO40,60^A0,110^FD{label_info[f"{pallet_label_field_2}"]}^FS
                ^FO470,480^A0,100^{label_info[f"{pallet_label_field_4}"]}^FS
                ^FO470,880^A0,100^FD{field_3}^FS
                ^XZ
                """
        return(zpl)
    except Exception as ex:
        print("Data could not be processed: \n", ex)
