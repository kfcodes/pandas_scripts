import os
from dotenv import load_dotenv
load_dotenv(".env")

def create_this_label(qty):
    print("create label function", qty)
    try:
        zpl = f"""
^XA
^CF0,50
^PQ{qty}
^FO60,35^FDCode:^FS
^FO60,120^FDProduct:^FS
^FO50,95^GB700,3,3^FS
^XZ
"""
        return(zpl)
    except Exception as ex:
        print("Data could not be processed: \n", ex)
