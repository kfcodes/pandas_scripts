import os
from dotenv import load_dotenv
load_dotenv(".env")

def create_combined_pallet_label_outline():
    try:
        zpl = """
^XA^CFD^FWR^LH20,20
^PQ2,10,1,Y
^FO630,220^A0,100^FDCOMBINED PALLET^FS
^FO520,480^A0,60^FDPALLETS^FS
^FO250,10^GB360,1170,5^FS
^FO90,30^A0,55^FDGROSS^FS
^FO30,30^A0,55^FDWEIGHT^FS
^FO65,450^A0,60^FDKG^FS
^FO10,10^GB180,530,5^FS
^FO100,620^A0,60^FDGROSS^FS
^FO30,620^A0,60^FDHEIGHT^FS
^FO65,1060^A0,60^FDCM^FS
^FO10,580^GB180,580,5^FS
"""
        return(zpl)
    except Exception as ex:
        print("Data could not be processed: \n", ex)

def create_combined_pallet_label_data(label_info):
    try:
        zpl = f"""
^FO50,260^A0,80^FD${label_info.weight}^FS
^FO50,860^A0,80^FD${label_info.height}^FS
^FO350,80^A0,70^FD ${label_info.pallets}^FS
^XZ"""
        return(zpl)
    except Exception as ex:
        print("Data could not be processed: \n", ex)
