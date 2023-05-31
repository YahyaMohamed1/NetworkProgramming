from socket import *
S = socket(AF_INET, SOCK_STREAM)
#AF_INET is the address family for IPv4
#SOCK_STREAM is the socket type for TCP
host= "127.0.0.1"
#host is the IP address of the server
port = 7000
#port is the port number of the server
S.bind((host, port))
#bind() is used to associate the socket with a specific network interface and port number
S.listen(5)
while True:
    C, addr = S.accept()
    #C is the client socket
    #addr is the client address
    print('Got connection from', addr)
    #print the client address
    C.send(b'Thank you for connecting')
    #send the data to the client
    x=C.recv(1024)
    #x is the data received from the client
    print(x)
    #print the data received from the client
    C.close()
    #close the connection
