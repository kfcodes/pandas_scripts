import os
from dotenv import load_dotenv
load_dotenv(".env")

def create_large_product_label_2(data):
    try:
        zpl = f"""
^XA^CFD^FWR^LH2,10
^FO610,120^GB170,900,5^FS
^FO20,10^GB120,1175,5^FS
^FO20,325^GB120,,5^FS
^FO20,645^GB120,,5^FS

^CF0,150
^FO600,300^FD{data["company"]}^FS

^CF0,100
^FO450,50^FD{data["product"]}^FS

^CF0,90
^FO300,330^FD{data["flavour"]}^FS

^CF0,110
^FO150,350^FDQTY: {data["quantitiy"]}^FS

^CF0,60
^FO40,30^FDLOT: {data["lot"]}^FS
^FO40,355^FDBBE: {data["bbe"]}^FS
^FO40,675^FDBATCH: {data["batch"]}^FS

^XZ"""
        return(zpl)
    except Exception as ex:
        print("data could not be processed: \n", ex)
