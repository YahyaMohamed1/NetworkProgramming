import threading
import socket
host = '127.0.0.1'
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
aliases = []

def broadcast(message): # Function to broadcast the message to all clients
    for client in clients:
        client.send(message)

def handle_client(client): # Function to handle clients'connections
    while True:
        try: # Broadcasting the message, if client exists in the chatroom, else removing the client from the list
            message = client.recv(1024) # Broadcasting the message
            broadcast(message)
        except: # Removing and closing the clients and removing the alias if the link is broken or the client is disconnected
            index = clients.index(client)  # Removing and closing the clients
            clients.remove(client)         # Removing the client
            client.close()                 # Closing the client
            alias = aliases[index]         # Removing the alias
            broadcast(f'{alias} has left the chat room!'.encode('utf-8')) # Broadcasting the message
            aliases.remove(alias)         # Removing the alias
            break

def receive(): # Main function to receive the clients'connections
    while True:
        print('Server is running and listening ...')
        client, address = server.accept()
        print(f'connection is established with {str(address)}')
        client.send('name alias:'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'The alias of this client is {alias}'.encode('utf-8'))
        broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))
        client.send('you are now connected!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,)) # Creating a thread for each client that connects to the server
        thread.start() # Starting the thread


if __name__ == "__main__":
    receive()
