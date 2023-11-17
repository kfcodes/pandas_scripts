import socket              

import os
from dotenv import load_dotenv
load_dotenv(".env")

mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         

def print_large_label(label_data):
	try:
		host = os.getenv("BIGLABELID1") 
		port = os.getenv("BIGLABELPORT1") 
		# mysocket.connect((host, port)) #connecting to host
		# mysocket.send(b"^XA^A0N,50,50^FO50,50^FDSocket Test^FS^XZ")#using bytes
		# mysocket.close () #closing connection
		print(f"Printed the Label to {host}, {port} \n {label_data}")

	except Exception as ex:
		print("Could not print label due to the following: \n", ex)

def print_small_label(label_data):
	try:
		print(label_data)
		host1 = os.getenv("SMALLLABELPRINTER1") 
		port1 = os.getenv("SMALLLABELPRINTERPORT1") 
		port1 = int(port1)
		label =  label_data.encode(encoding="ascii",errors="ignore")
		mysocket.connect((host1, port1)) #connecting to host
		mysocket.send(label)#using bytes
		mysocket.close () #closing connection
		# print(f"Printed the Label to {host1}, {port1} \n {label}")
		print(f"Printed the Label to {host1}, {port1}")

	except Exception as ex:
		print("Could not print label due to the following: \n", ex)
