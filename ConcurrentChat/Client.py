import threading
import socket


alias = input('Alias? ') # Getting the a

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))


def client_receive(): # Function to receive the messages from the server
    while True:       # Listening for any messages from the server
        try:          # If the message is "alias?", client will send the alias
            message = client.recv(1024).decode('utf-8') # If not, will print the message
            if message == "alias?": # If the message is "alias?", client will send the alias
                client.send(alias.encode('utf-8')) # If not, will print the message
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive) # Creating a thread for the client to listen to the messages coming from the server
receive_thread.start()                                   # Starting the thread

send_thread = threading.Thread(target=client_send)      # Creating a thread for the client to send messages to the server
send_thread.start()                                     # Starting the thread
