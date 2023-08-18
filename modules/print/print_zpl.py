import socket              

mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         

try:           
	mysocket.connect((host, port)) #connecting to host
	# mysocket.send(b"^XA^A0N,50,50^FO50,50^FDSocket Test^FS^XZ")#using bytes
	# mysocket.send(b"^XA^A0N,50,50^FO50,50^FDSocket Test^FS^XZ")#using bytes
	mysocket.send(b"^XA^A0N,50,50^FO50,50^FDTest^FS^XZ")#using bytes
	mysocket.close () #closing connection
except:
	print("Error with the connection")
