import socket              
import os
from dotenv import load_dotenv
load_dotenv("../../.env")

def print_large_label(label_data):
	try:
		# SETTING THE VARIABLES FOR THE FUNCTION
		host = os.getenv("BIGLABELID1") 
		port = int(os.getenv("BIGLABELPORT1"))
		label =  label_data.encode(encoding="ascii",errors="ignore")

		# CREATING THE SOCKET CONNECTION AND SENDING THE DATA
		mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         
		mysocket.connect((host, port)) #connecting to host
		mysocket.send(label) #using bytes
		mysocket.close () #closing connection

		return f"Printed the Label to {host}, {port}"
	except Exception as ex:
		print("Could not print label due to the following: \n", ex)
		return "Not printed"

def print_small_label(label_data):
	try:
		# host = os.getenv("SMALLLABELPRINTER1") 
		# port = os.getenv("SMALLLABELPRINTERPORT1") 
		# port = int(port)
		# label =  label_data.encode(encoding="ascii",errors="ignore")
		# mysocket.connect((host, port)) #connecting to host
		# mysocket.send(label)#using bytes
		# mysocket.close () #closing connection
		# return f"Printed the Label to {host}, {port}"
		print(label_data)
	except Exception as ex:
		print("Could not print label due to the following: \n", ex)
