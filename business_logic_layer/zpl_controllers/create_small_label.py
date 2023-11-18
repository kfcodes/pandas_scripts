import os
from dotenv import load_dotenv
load_dotenv("../../.env")

def create_small_label_outline():
    try:
        zpl = """
            ^XA^CFD^FWN
            ^FO10,70^GB795,10,7^FS
            ^CF0,30
            ^FO30,90 ^FDPRODUCT^FS
            ^FO30,130 ^FDFLAVOUR^FS
            ^FO30,170 ^FDQUANTITY^FS
            ^FO30,210 ^FDUNIT WEIGHT (KG)^FS
            ^FO30,250 ^FDBBE^FS
            ^FO30,290 ^FDLOT^FS
            ^FO30,330 ^FDBATCH^FS
            """

        return(zpl)

    except Exception as ex:
        print("Data could not be processed: \n", ex)

def create_small_label_data(label_info):

    try:
        zpl = f"""
            ^PQ3
            ^CF0,40
            ^FO30,25^FDCOMPANY NAME^FS
            ^CF0,30
            ^FO330,90 ^FDPRODUCT^FS
            ^FO330,130 ^FDFLAVOUR^FS
            ^FO330,170 ^FDQUANTITY^FS
            ^FO330,210 ^FDUNIT WEIGHT (KG)^FS
            ^FO330,250 ^FDBBE^FS
            ^FO330,290 ^FDLOT^FS
            ^FO330,330 ^FDBATCH^FS
            ^XZ
            """

        return(zpl)

    except Exception as ex:
        print("Data could not be processed: \n", ex)
