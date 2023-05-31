from socket import *
S = socket(AF_INET, SOCK_STREAM)
host= '127.0.0.1'
port = 7000
S.connect((host,port)) # Connect to the server
while True:
    data = input("Client: ")
    S.send(data.encode('utf-8')) # send the data to server
    data = S.recv(1024)
    if not data:
        break
    print("Server: ", data.decode('utf-8')) # print the data received from server
S.close() # close the connection
