from socket import *
try:
    S = socket(AF_INET, SOCK_STREAM)
    S.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # To avoid the error: OSError: [Errno 98] Address already in use

    host= '127.0.0.1'
    port = 7000
    S.bind((host,port)) # Bind the socket to the port
    S.listen(5) # Listen for the client connection
    print("Server is ready to listen")
    C, addr = S.accept() # Accept the connection from client
    print("Connection from: ", str(addr)) # print the address of the client
    while True:
        data = C.recv(1024)
        if not data:
            break
        print("Client: ", data.decode('utf-8')) # print the data received from client
        data = input("Server: ")
        C.send(data.encode('utf-8')) # send the data to client
    C.close() # close the connection
except Exception as e:
    print("Error: ", e)
except KeyboardInterrupt:
    print("Server is closed") # To close the server press Ctrl+C
