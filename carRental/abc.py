import tkinter as tk
from tkinter import *
import random
import time

root = Tk()
root.geometry("1300x600+0+0")
root.title("VENDING MACHINE")
root.configure(bg='peach puff')
lbl_title = tk.Label(root,text="SELECT YOUR ITEMS.", bg = 'peach puff')
lbl_title.pack()

text_Input = StringVar()
operator = ""

#==================================Setting the Frame=======================================


Tops = Frame(root, width=1000, height=50, bg="peach puff" )
Tops.pack(side=TOP)

Topss = Frame(root, width=1000, height=50, bg="peach puff" )
Topss.pack(side=TOP)

f1 = Frame(root, width=1200, height=700, bg="peach puff")
f1.pack(side=LEFT)

#f2 = Frame(root, width=300, height=700, bg="peach puff")
#f2.pack(side=RIGHT)


lblInfo = Label(Tops, font=('simplifica', 50, 'bold'), text="VENDING MACHINE", fg="Black", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)


def new_window():
    top=Toplevel()
    top.geometry("1000x600+0+0")
    top.title("LAYS")
    top.configure(bg='peach puff')
    lblInfo0 = Label(top, font=('simplifica', 50, 'bold'), text="LAYS FLAVOUR", fg="Black", bd=10, anchor='w')
    lblInfo0.grid(row=0, column=4)

    button6 = Button(top, font=('arial', 16, 'bold'), text='CREAM AND ONION',bg = 'peach puff',bd=19)
    button6.grid(row=2,column=0)
    button7= Button(top, font=('arial', 16, 'bold'), text='TANGY TOMATO',bg = 'peach puff',bd=19)
    button7.grid(row=3,column=0)
    button8 = Button(top, font=('arial', 16, 'bold'), text='MASALA MAGIC',bg = 'peach puff',bd=19)
    button8.grid(row=4,column=0)
    button9 = Button(top, font=('arial', 16, 'bold'), text='SALT',bg = 'peach puff',bd=19)
    button9.grid(row=5,column=0)
   

def new_window1():
    qwe=Toplevel()
    qwe.geometry("1300x600+0+0")
    qwe.title("SOFTDRINKS")
    qwe.configure(bg='peach puff')


def new_window2():
    abc=Toplevel()
    abc.geometry("1300x600+0+0")
    abc.title("CANDY")
    abc.configure(bg='peach puff')

def new_window3():
    aaa=Toplevel()
    aaa.geometry("1300x600+0+0")
    aaa.title("CHOCOLATE")
    aaa.configure(bg='peach puff')







LAYS=DoubleVar()
SOFTDRINKS=DoubleVar()
CANDY=DoubleVar()
CHOCOLATES=DoubleVar()

button1 = Button(f1, font=('arial', 16, 'bold'), text='LAYS',bg = 'peach puff',bd=19,command=new_window)
button1.grid(row=0,column=0)

button2 = Button(f1, font=('arial', 16, 'bold'), text='SOFTDRINKS', bg = 'peach puff',bd=19,command=new_window1)
button2.grid(row=1,column=0)

button3 = Button(f1, font=('arial', 16, 'bold'), text='CANDY', bg = 'peach puff',bd=19,command=new_window2)
button3.grid(row=2,column=0)

button4 = Button(f1,font=('arial',16,'bold'), text="CHOCOLATE", bg = 'peach puff',bd=19,command=new_window3)
button4.grid(row=3,column=0)

button5=Button(f1,font=('arial',16,'bold'),text="EXIT",bg='peach puff',bd=19,command=exit)
button5.grid(row=4,column=0)
 
def exit():
    root.destroy()

    
root.mainloop()