import cups
import os
from dotenv import load_dotenv
load_dotenv("../../.env")

def print_a4_pdf(file_path):

    printer_name = os.getenv('A4PRINTER')

    conn = cups. Connection()
    printers = conn.getPrinters()
    
    if printer_name in printers:
        try:
            conn.printFile(printer_name, file_path, "Print Job", {})
            print("File sent to printer successfully.")
        except cups.IPPError as e:
            print(f"Error printing file: {e}")
    else:
        print(f"Printer '{printer_name}' not found.")
