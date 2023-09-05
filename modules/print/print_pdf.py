import os
from dotenv import load_dotenv
load_dotenv("../../.env")

def print_pdf():
	try:

	except Exception as ex:
		print("Could not print pdf file due to the following: \n", ex)
