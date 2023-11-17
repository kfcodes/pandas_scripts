import socket              
import os
from dotenv import load_dotenv
load_dotenv(".env")
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         

def print_large_label():
	try:
		host = os.getenv("BIGLABELID1") 
		port = os.getenv("BIGLABELPORT1") 
		# mysocket.connect((host, port)) #connecting to host
		# mysocket.send(b"^XA^A0N,50,50^FO50,50^FDSocket Test^FS^XZ")#using bytes
		# mysocket.close () #closing connection
		print(f"Printed the Label to {host}, {port}")

	except Exception as ex:
		print("Could not print label due to the following: \n", ex)

def print_small_label():
	try:
		host = os.getenv("SMALLLABELPRINTER1") 
		port = os.getenv("SMALLLABELPRINTERPORT1") 
		# mysocket.connect((host, port)) #connecting to host
		# mysocket.send(b"^XA^A0N,50,50^FO50,50^FDSocket Test^FS^XZ")#using bytes
		# mysocket.close () #closing connection
		print(f"Printed the Label to {host}, {port}")

	except Exception as ex:
		print("Could not print label due to the following: \n", ex)
