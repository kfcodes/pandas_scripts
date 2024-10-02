import os
from dotenv import load_dotenv
load_dotenv(".env")

def create_large_product_label(data, qty):
    try:
        print(data)
        zpl = f"""
^XA

^PQ{qty},10,1,Y

^CF0,50
^FO210,30^FD{data["brand"]}^FS
^FO380,30^FD{data["product"]}^FS
^FO210,85^FD{data["flavour"]}^FS

^CF0,40
^FO50,180^FDSKU: {data["sku"]}^FS
^FO50,230^FDBATCH: {data["eol_lot"]}^FS
^FO50,280^FDBB:  {data["eol_bbe"]}^FS

^BY2
^FO390,220
^BCN,120,Y,N,N,N,N
^FD{data["box_barcode"]}^FS

^XZ"""
        return(zpl)
    except Exception as ex:
        print("data could not be processed: \n", ex)
