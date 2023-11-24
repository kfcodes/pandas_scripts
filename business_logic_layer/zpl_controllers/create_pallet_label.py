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
