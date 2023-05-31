import tkinter
from tkinter import *
from tkinter import messagebox
import socket

root = tkinter.Tk()

def reset():
    e1.delete(0, END)

def checkans():
    var = e1.get().strip()  # Remove any leading/trailing whitespaces

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8000))

    word = client_socket.recv(1024).decode()
    label.config(text=word)

    client_socket.sendall(var.encode())
    result = client_socket.recv(1024).decode()
    result = bool(result)

    client_socket.close()

    if result:
        messagebox.showinfo("Congratulations", "It's the correct answer!!")
    else:
        messagebox.showerror("Sorry", "It's not the correct answer.")

    reset()

root.geometry("500x500+500+150")
root.title("Jumbled word game")
root.configure(background="#000000")

Label(root, text="JUMBLED WORD GAME", font=("Verdana", 28), bg="#000000", fg="#fff").pack(pady=5)
label = Label(root, font=("Verdana", 22), bg="#000000", fg="#fff")
label.pack(pady=30, ipady=10, ipadx=10)

ans = StringVar()
e1 = Entry(root, font=("Verdana", 20), textvariable=ans)
e1.pack(ipady=5, ipadx=5)

Button(root, text="Check", font=("Comic sans ms", 20), width=10, bg="#333945", fg="#45CE30", relief=GROOVE, command=checkans).pack(pady=40)
Button(root, text="Reset", font=("Comic sans ms", 20), width=10, bg="#777E8B", fg="#E1DA00", relief=GROOVE, command=reset).pack()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8000))

word = client_socket.recv(1024).decode()
label.config(text=word)

client_socket.close()

root.mainloop()
