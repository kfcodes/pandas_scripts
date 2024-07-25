# import cups

import os
from dotenv import load_dotenv
load_dotenv("../.env")

def print_a4_pdf(file):
    printer = os.getenv('A4PRINTER')
    printer_connection = cups.Connection()
    printers = printer_connection.getPrinters()
    
    if printer in printers:
        try:
            printer_connection.printFile(printer, file, "Print Job", {})
            print("File sent to printer")
        except cups.IPPError as e:
            print(f"Error printing file: {e}")
    else:
        print(f"Printer '{printer}' not found.")
