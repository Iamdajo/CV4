import tkinter
from random import*
canvas=tkinter.Canvas(bg="white",width=600,height=600)
canvas.pack()

def listok(x,y):
    canvas.create_rectangle(x-10,y-5,x+10,y+10,fill="green",tag="listok")

def generuj_l():
    global x_listok
    canvas.delete("text")
    canvas.delete("all")
    x_listok=randrange(30,600,60)
    listok(x_listok,y)
button1=tkinet.Button(text
