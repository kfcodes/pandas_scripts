import os
from dotenv import load_dotenv
load_dotenv(".env")

def create_this_label(qty):
    print("create label function", qty)
    try:
        zpl = f"""
^XA
^FX LEFT SECTION WITH THIS WAY UP SYMBOL
^FO130,45^GFA,28490,28490,70,,::::::::::::kG0F,kG0F8,::::::::::,:::::::::::kG0F,kG0F8,::::::::::,::::::::lR01FF8,::kG0F8gO01FF8,::::::::::kG0FgP01FF8,lH03RF8,00LFkT03RF8,01LFiM0ChL03RF8,01LFiM0EhL03RF8,01LFiM0F8hK03RF8,01LFiM0FEhK03RF8,01LFiM0FF8hJ03RF8,01LFiM0FFEhJ03RF8,01LFiM0IFhJ03RF8,01LFiM0IFChI03RF8,01LFiM0JFhI03RF8,01LFiM0JFChR01FF8,01LFiM0KFgG0F8gO01FF8,01LFiM0KF8g0F8gO01FF8,01LFiM0KFEg0F8gO01FF8,01LFiM0LF8Y0F8gO01FF8,01LFiM0LFEY0F8gO01FF8,01LFiM0MFY0F8gO01FF8,01LFiM0MFCX0F8gO01FF8,01LFiM0NFX0F8gO01FF8,01LFiM0NFCW0F8gO01FF8,01LFiM0OFW0F8gO01FF8,01LFiM0OF8V0F8gO01FF8,01LFiM0OFEV0FgP01FF8,01LFiM0PF8hL01FF8,01LFiM0PFEhL01FF8,01LFiM0QF8,01LFK0iSFC,01LFK0iTF,01LFK0iTFC,01LFK0iUF,01LFK0iUFCgS03RF,01LFK0iUFEgS03RF8,01LFK0iVF8gR03RF8,01LFK0iVFEgR03RF8,01LFK0iWF8P0Fg03RF8,01LFK0iWFCP0F8Y03RF8,01LFK0iXFP0F8Y03RF8,01LFK0iXFCO0F8Y03RF8,01LFK0iYFO0F8Y03RF8,01LFK0iYFCN0F8Y03RF8,01LFK0iYFEN0F8gK07FC,01LFK0jF8M0F8gL0FE,01LFK0jFEM0F8gL03F,01LFK0jGF8L0F8gL01F8,01LFK0jGFEL0F8gL01FC,01LFK0jHFL0F8gL01FC,01LFK0jHFCgS01FE,01LFK0jIFgT0FE,01LFK0jIFCgR01FE,01LFK0jJFgR01FE,01LFK0jJF8gQ01FE,01LFK0jJFEgQ01FF,01LFK0jJFEgQ03FF,01LFK0jJFCgQ0FFE,01LFK0jJFgK03NFE,01LFK0jIFCgK03NFE,01LFK0jIFgL03NFE,01LFK0jHFEgL03NFE,01LFK0jHF8K0F8Y03NFC,01LFK0jGFEL0F8Y03NF8,01LFK0jGF8L0F8Y03NF8,01LFK0jFEM0F8Y03NF,01LFK0jFCM0F8Y03MFC,01LFK0jFN0F8Y03MF,01LFK0iYFCN0F8,01LFK0iYFO0F8,01LFK0iXFEO0F8,01LFK0iXF8O0F8,01LFK0iWFEP0F8,01LFK0iWF8P0F8,01LFK0iWF,01LFK0iVFC,01LFK0iVFgS03NFC0FF,01LFK0iUFCgS03NFE0FF8,01LFK0iUFgT03NFE0FF8,01LFK0iTFEgT03NFE0FF8,01LFK0iTF8gT03NFE0FF8,01LFK0iSFEgU03NFE0FF8,01LFiL01QF8gU03NFE0FF8,01LFiM0QFgV03NFE0FF8,01LFiM0PFCgV03NFE0FF8,01LFiM0PFgW03NFE0FF8,01LFiM0OFCV0F8,01LFiM0OF8V0F8,01LFiM0NFEW0F8,01LFiM0NF8W0F8,01LFiM0MFEX0F8,01LFiM0MF8X0F8,01LFiM0LFEY0F8gH04,01LFiM0LFCY0F8gG07C003C,01LFiM0LFg0F8g01FC01FF8,01LFiM0KFCg0F8g03FC03FFE,01LFiM0KF8g0F8N07LFK07FC07IF,01LFiM0JFEgG0FN07MFK0FFC07IF8,01LFiM0JF8gO01NFK0FFC0JF8,01LFiM0IFEgP03NFJ01FFC0JFC,01LFiM0IF8gP07NFJ03FFC1JFC,01LFiM0IFgQ0OFJ03FFC1JFE,01LFiM0FFCgQ0OFJ03FF01JFE,01LFiM0FFgQ01OFJ03FC03FFBFE,01LFiM0FCgQ01OFJ07F803FE0FE,01LFiM0F8gQ01OFJ07F803FE0FE,01LFiM0EgR01IF8O07F003FC07E,01LFiM08gR01FF8P07F007FC07F,01LFk01FFQ07F007F807F,01LFk03FEQ07F007F807F,01LFjS0F8K01FEQ07F007F807F,01LFjS0F8K01FEQ07F00FF807E,01LFjS0F8K01FCQ07F00FF80FE,01LFjS0F8K01FCQ07F80FF00FE,01LFjS0F8K01FEQ07F81FF01FE,01LFjS0F8L0FEQ07FC3FF07FE,01LFjS0F8L0FEQ03KF0FFE,01LFjS0F8L07FQ03JFE0FFC,01LFjS0F8L03F8P03JFE0FFC,01LFjS0F8L01FEP01JFE0FF8,01LFjS0F8M0NFJ01JFC0FF8,01LFjS0FL01OFK0JFC0FF,01LFk01OFK07IF80FE,01LFk01OFK03IF00FC,01LFk01OFK01FFE00F,01LFk01OFL07FC,01LFk01OF,:::01LFkG04,01LF,:01LFjS0F,01LFjS0F8,:::01LFjS0F8001RF,::::::01LFjW01RF,::01LFkG01FF801FF,01LFkG03FCI07FCR01E,01LFkG07F8I01FCR0FE,01LFkG07FK0FEQ07FE,01LFkG0FEK0FFP07FFE,01LFkG0FEK07FO03IFE,01LFk01FCK07F8M01JFE,01LFk01FCK07F8M0KFE,01LFk01FCK07F8L07KFE,01LFjS0F8K01FCK07F8K03LFE,01LFjS0F8K01FCK07F8J01MFE,01LFjS0F8K03FEK07F8I01NF8,01LFjS0F8K01FEK0FF8I03MF8,01LFjS0F8K01FFK0FF8I03LF8,01LFjS0F8K01FF8I01FF8I03KFC,01LFjS0F8K01FFCI07FF8I03JFC,01LFiM0CgK0F8K01IF801IFJ03IFC,01LFiM0FgK0F8L0OFJ03FFE,01LFiM0F8gJ0F8L0NFEJ03IF8,01LFiM0FEgJ0F8L07MFEJ03JF8,01LFiM0FF8gI0F8L07MFCJ03KF8,01LFiM0FFEgQ03MF8J03LF8,01LFiM0IFgQ01MFK03MF8,01LFiM0IFCgQ0LFEL03MF8,01LFiM0JFgQ03KF8M03LFE,01LFiM0JFCgQ0JFEO03KFE,01LFiM0KFgQ01IFQ03JFE,01LFiM0KF8hL03IFE,01LFiM0KFEhM07FFE,01LFiM0LF8hK01IFE,01LFiM0LFEhK0JFE,01LFiM0MF8hI0KFE,01LFiM0MFChH0LFE,01LFiM0NFX0F8gG0MFC,01LFiM0NFCW0F8g07LFE,01LFiM0OFW0F8Y03MF,01LFiM0OFCV0F8Y03LF,01LFiM0OFEV0F8Y03JFE,01LFiM0PF8U0F8Y03JF,01LFiM0PFEU0F8Y03FFE,01LFiM0QF8T0F8Y03FFE,01LFK0iSFET0F8Y03IFE,01LFK0iTFT0F8Y03JFE,01LFK0iTFCS0F8Y03KFE,01LFK0iUFS0Fg03LFE,01LFK0iUFCgS03MFC,01LFK0iVFgT07MFC,01LFK0iVF8gT0MFE,01LFK0iVFEgT01LFE,01LFK0iWF8gT03KFE,01LFK0iWFEgU07JFE,01LFK0iXFgV07IFE,01LFK0iXFCgV0IFE,01LFK0iYFgV01FFE,01LFK0iYFCgV03FE,01LFK0jFgW07E,01LFK0jF8M08gO0E,01LFK0jFEM0F8,01LFK0jGF8L0F8,01LFK0jGFEL0F8,01LFK0jHFL0F8g01FF,01LFK0jHFCK0F8g03FFC01E,01LFK0jIFK0F8g0JF01F8,01LFK0jIFCJ0F8g0JF01FC,01LFK0jJFJ0F8Y01JF81FF,01LFK0jJF8I0F8Y03JF81FF,01LFK0jJFEI0F8Y03JFC1FF8,:01LFK0jJF8I07g07JFC1FFC,01LFK0jJFgK07JFE1FFC,01LFK0jIFCgK07FC1FE1FFE,01LFK0jIFgL07F80FE07FE,01LFK0jHFCgL07F007E01FE,01LFK0jHF8gL07F007E00FE,01LFK0jGFEgM07F007E00FE,01LFK0jGF8gM07F003F007E,01LFK0jFEgN07F003F007F,01LFK0jFCgN03F003F007F,01LFK0jFgO03F003F007F,01LFK0iYFCgO03F003F007F,01LFK0iYFO0Fg01F801F007E,01LFK0iXFCO0F8Y01F801F80FE,01LFK0iXF8O0F8g0FE01F80FE,01LFK0iWFEP0F8g07F81FC3FE,01LFK0iWF8P0F8g07MFE,01LFK0iVFEQ0F8Y03NFE,01LFK0iVFCQ0F8Y03NFE,01LFK0iVFR0F8Y03NFC,01LFK0iUFCR0F8Y03NFC,01LFK0iUFS0F8Y03NF8,01LFK0iTFES0F8Y03NF8,01LFK0iTF8S0F8Y03NF,01LFK0iSFEgU03MFE,01LFiL01QF8gU03MF8,01LFiM0PFEgV038,01LFiM0PFC,01LFiM0PF,01LFiM0OFC,01LFiM0OFhM0E,01LFiM0NFEhL07E,01LFiM0NF8hK01FE,01LFiM0MFEgV07FCM0FFE,01LFiM0MF8gV07FCL07FFE,01LFiM0LFEgW07FCK01IFE,01LFiM0LFCY0F8V07FCK0JFE,01LFiM0LFg0F8V07F8J07JFE,01LFiM0KFCg0F8V07FCI01KFE,01LFiM0KFgG0F8V07FCI0LFE,01LFiM0JFEgG0F8V07FC007LFC,01LFiM0JF8gG0F8V07FE01LFE,01LFiM0IFEgH0F8V07FF0MF,01LFiM0IF8gH0F8V07OF8,01LFiM0FFEgI0F8V03NFC,01LFiM0FFCgI0F8V03MFE,01LFiM0FFgJ0F8V01MF,01LFiM0FCgJ0F8V01LF8,01LFiM0FhJ0KFE,01LFiM0EhJ07KF,01LFiM08hJ01KFE,lG0LFC,lG01LFC,lH03LF8,lI07LF,lI01LFE,lJ03LFC,lK0LFE,lK01KFE,lL03JFE,kG0F8gJ07IFE,kG0F8gJ01IFE,kG0F8gK03FFE,kG0F8gL07FE,kG0F8gL01FE,kG0F8gM03E,kG0F8gN06,kG0F8,:::kG0F,,:::::::::::kG0F8,::::::::::,:::::::::::kG0F,kG0F8,::,:::::::::^FS

^FX LABEL QUANTITY AND OUTLINE BOXES
^PQ{qty}
^FO50,40^GB700,420,6^FS
^FO50,470^GB700,700,6^FS
^FO50,785^GB480,6,6^FS

^FX DATA LABELS WITH A SERIES OF DIVIDING LINES BETWEEN
^FO620,470^GB6,700,6^FS
^FO530,470^GB3,700,3^FS
^FO461,501^A0R,50,50^FDQuantity^FS
^FO460,500^A0R,50,50^FDQuantity^FS
^FO450,470^GB3,700,3^FS
^FO381,500^A0R,50,50^FDUnit Weight^FS
^FO380,500^A0R,50,50^FDUnit Weight^FS
^FO370,470^GB3,700,3^FS
^FO301,501^A0R,50,50^FDERP Number^FS
^FO300,500^A0R,50,50^FDERP Number^FS
^FO290,470^GB3,700,3^FS
^FO221,501^A0R,50,50^FDPO Number^FS
^FO220,500^A0R,50,50^FDPO Number^FS
^FO210,470^GB3,700,3^FS
^FO140,501^A0R,50,50^FDLOT^FS
^FO140,500^A0R,50,50^FDLOT^FS
^FO130,470^GB3,700,3^FS
^FO60,501^A0R,50,50^FDBBE^FS
^FO60,500^A0R,50,50^FDBBE^FS

^FX UNIQUE PRODUCT IDENTIFICATION INFORMATION
^FO615,630^A0R,110,110^FD{company}^FS
^FO616,631^A0R,110,110^FD{company}^FS
^FO617,632^A0R,110,110^FD{company}^FS
^FO540,520^A0R,60,60^FD{product_description}^FS
^FO460,880^A0R,45,45^FD{quantity} UNITS^FS
^FO380,880^A0R,45,45^FD{weight}G^FS
^FO300,880^A0R,45,45^FD{product_code}^FS
^FO220,880^A0R,45,45^FD{po}^FS
^FO140,880^A0R,45,45^FD{lot}^FS
^FO60,880^A0R,45,45^FD{bbe}^FS
^XZ
"""
        return(zpl)
    except Exception as ex:
        print("Data could not be processed: \n", ex)