#Client.py
from socket import *
S = socket(AF_INET, SOCK_STREAM)
#AF_INET is the address family for IPv4
#SOCK_STREAM is the socket type for TCP
host= "127.0.0.1"
#host is the IP address of the server
port = 7000
#port is the port number of the server
S.connect((host, port))
#connect() is used to connect to the server
x=S.recv(1024)
#x is the data received from the server
print(x)
#print the data received from the server
S.send(b'Hello server')
#send the data to the server
S.close()
#close the connection



