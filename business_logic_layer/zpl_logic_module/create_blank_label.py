import os
from dotenv import load_dotenv
load_dotenv(".env")

def create_blank_label_outline():
    try:
        zpl = """

                ^XA^CFD
                ^FWR
                ^LH30,20
                ^PQ1000,10,1,Y
                ^FO550,10^GB160,1170,5^FS
                ^FO630,10^GB5,1170,5^FS
                ^FO640,20^A0,40^FDPRODUCT:^FS
                ^FO565,20^A0,40^FDLOT:^FS
                ^FO565,300^A0,40^FDBBE:^FS
                ^FO565,550^A0,40^FDBATCH:^FS
                ^FO565,920^A0,40^FDQTY:^FS
                ^FO370,10^GB160,1170,5^FS
                ^FO450,10^GB5,1170,5^FS
                ^FO460,20^A0,40^FDPRODUCT:^FS
                ^FO395,20^A0,40^FDLOT:^FS
                ^FO395,300^A0,40^FDBBE:^FS
                ^FO395,550^A0,40^FDBATCH:^FS
                ^FO395,920^A0,40^FDQTY:^FS
                ^FO195,10^GB160,1170,5^FS
                ^FO275,10^GB5,1170,5^FS
                ^FO285,20^A0,40^FDPRODUCT:^FS
                ^FO215,20^A0,40^FDLOT:^FS
                ^FO215,300^A0,40^FDBBE:^FS
                ^FO215,550^A0,40^FDBATCH:^FS
                ^FO215,920^A0,40^FDQTY:^FS
                ^FO15,10^GB160,1170,5^FS
                ^FO95,10^GB5,1170,5^FS
                ^FO105,20^A0,40^FDPRODUCT:^FS
                ^FO30,20^A0,40^FDLOT:^FS
                ^FO30,300^A0,40^FDBBE:^FS
                ^FO30,550^A0,40^FDBATCH:^FS
                ^FO30,920^A0,40^FDQTY:^FS
                ^XZ

            """
        return(zpl)
    except Exception as ex:
        print("Data could not be processed: \n", ex)
