# from fpdf import FPDF

import os
from dotenv import load_dotenv
load_dotenv("../../.server_config_files/fastAPI.env")

def create_certificate_pdf(data):
    try:
        return (data)
    except Exception as ex:
        print("Data could not be processed: \n", ex)
