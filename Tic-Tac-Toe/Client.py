from tkinter import *
import random
import socket
from threading import Thread


def creat_thread(target):
    thread=Thread(target=target)
    thread.daemon=True #close the thread when the main program ends
    thread.start()     #start the thread

host ='127.0.0.1'
port = 7000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


def send_data(row, col):
    s.send(f"{row},{col}".encode("utf-8"))




def next_turn(row, col):
    global player
    if game_btns[row][col]['text'] == "" and check_winner() == False:
        if player == players[0]:
            # Put player 1 sympol
            game_btns[row][col]['text'] = player
            send_data(str(row)+str(col))

            if check_winner() == False:
                # switch player
                player = players[1]
                label.config(text=(players[1] + " turn"))

            elif check_winner() == True:
                label.config(text=(players[0] + " wins!"))

            elif check_winner() == 'tie':
                label.config(text=("Tie, No Winner!"))

        elif player == players[1]:
            # Put player 2 sympol
            game_btns[row][col]['text'] = player

            if check_winner() == False:
                # switch player
                player = players[0]
                label.config(text=(players[0] + " turn"))

            elif check_winner() == True:
                label.config(text=(players[1] + " wins!"))

            elif check_winner() == 'tie':
                label.config(text=("Tie, No Winner!"))


def check_winner():
    # check all 3 horizontal conditions
    for row in range(3):
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] != "":
            game_btns[row][0].config(bg="cyan")
            game_btns[row][1].config(bg="cyan")
            game_btns[row][2].config(bg="cyan")
            return True

    # check all 3 vertical conditions
    for col in range(3):
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] != "":
            game_btns[0][col].config(bg="cyan")
            game_btns[1][col].config(bg="cyan")
            game_btns[2][col].config(bg="cyan")
            return True

    # check diagonals conditions
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "":
        game_btns[0][0].config(bg="cyan")
        game_btns[1][1].config(bg="cyan")
        game_btns[2][2].config(bg="cyan")
        return True
    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "":
        game_btns[0][2].config(bg="cyan")
        game_btns[1][1].config(bg="cyan")
        game_btns[2][0].config(bg="cyan")
        return True

    # if there are no empty spaces left
    if check_empty_spaces() == False:
        for row in range(3):
            for col in range(3):
                game_btns[row][col].config(bg='red')
                send_data(row, col)

        return 'tie'

    else:
        return False


def check_empty_spaces():
    spaces = 9

    for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def start_new_game():
    global player
    player = random.choice(players)

    label.config(text=(player + " turn"))

    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text="", bg="#F0F0F0")

def recieve_data():
    while True:
        data = s.recv(1024).decode("utf-8")
        data = data.split(",")
        row = int(data[0])
        col = int(data[1])
        next_turn(row, col)

creat_thread(recieve_data)

window = Tk()
window.title("Tic-Tac-Toe")

players = ["x", "o"]
player = random.choice(players)

game_btns = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

label = Label(text=(player + " turn"), font=('consolas', 40))
label.pack(side="top")

restart_btn = Button(text="restart", font=('consolas', 20), command=start_new_game)
restart_btn.pack(side="top")

btns_frame = Frame(window)
btns_frame.pack()

for row in range(3):
    for col in range(3):
        game_btns[row][col] = Button(btns_frame, text="", font=('consolas', 50), width=4, height=1,
                                     command=lambda row=row, col=col: send_data(row, col))
        game_btns[row][col].grid(row=row, column=col)

window.mainloop()
