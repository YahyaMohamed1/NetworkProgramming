import random
import socket

answers = ["apple", "mango", "banana", 'achieve', 'kolkata', 'evening']
words = ['plpea', 'gnoma', 'annaba', 'hveeica', 'lkaatko', 'egvnine']

def reset():
    global words, answers, num
    num = random.randrange(0, len(words), 1)
    return words[num]

def checkans(var):
    global words, answers, num
    num = int(num)
    var = var.strip()  # Remove any leading/trailing whitespaces
    if var == answers[num]:
        return True
    else:
        return False

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8000))
    server_socket.listen(1)

    print("Server is listening for connections...")

    while True:
        client_socket, address = server_socket.accept()
        print("Client connected:", address)

        word = reset()
        client_socket.sendall(word.encode())

        while True:
            var = client_socket.recv(1024).decode()
            if not var:
                break
            result = checkans(var)
            client_socket.sendall(str(result).encode())

        client_socket.close()

if __name__ == '__main__':
    main()
