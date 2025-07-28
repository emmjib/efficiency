from tkinter import *
import random

root = Tk()
root.geometry("300x300")
root.title("Rock Paper Scissor Game")

computer_value = {"0": "Rock", "1": "Paper", "2": "Scissor"}

def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text="Player")
    l3.config(text="Computer")
    l4.config(text="")

def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"

def isrock():
    c_v = computer_value[str(random.randint(0, 2))]
    match_result = "Match Draw" if c_v == "Rock" else "Player Win" if c_v == "Scissor" else "Computer Win"
    l4.config(text=match_result)
    l1.config(text="Rock")
    l3.config(text=c_v)
    button_disable()

def ispaper():
    c_v = computer_value[str(random.randint(0, 2))]
    match_result = "Match Draw" if c_v == "Paper" else "Computer Win" if c_v == "Scissor" else "Player Win"
    l4.config(text=match_result)
    l1.config(text="Paper")
    l3.config(text=c_v)
    button_disable()

def isscissor():
    c_v = computer_value[str(random.randint(0, 2))]
    match_result = "Computer Win" if c_v == "Rock" else "Match Draw" if c_v == "Scissor" else "Player Win"
    l4.config(text=match_result)
    l1.config(text="Scissor")
    l3.config(text=c_v)
    button_disable()

Label(root, text="Rock Paper Scissor", font="normal 20 bold", fg="blue").pack(pady=20)

frame = Frame(root)
frame.pack(fill=X, padx=20)

l1 = Label(frame, text="Player", font=10)
l1.pack(side=LEFT)

l2 = Label(frame, text="VS", font="normal 10 bold")
l2.pack(side=LEFT, expand=True, padx=40)

l3 = Label(frame, text="Computer", font=10)
l3.pack(side=RIGHT)

l4 = Label(root, text="", font="normal 20 bold", bg="white", width=15, borderwidth=2, relief="solid")
l4.pack(pady=20)

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1, text="Rock", font=10, width=7, command=isrock)
b2 = Button(frame1, text="Paper ", font=10, width=7, command=ispaper)
b3 = Button(frame1, text="Scissor", font=10, width=7, command=isscissor)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

Button(root, text="Reset Game", font=10, fg="red", bg="black", command=reset_game).pack(pady=20)

root.mainloop()
