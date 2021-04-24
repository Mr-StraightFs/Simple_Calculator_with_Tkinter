import tkinter
from tkinter import *

root = Tk()
root.title="Simple Calculator"
e=Entry(root , width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    if number == "clear" :
        e.delete(0, END)
        return
    current= e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    return


def button_add():
    global operation
    global f_number
    operation = "add"
    f_number = float(e.get())
    e.delete(0,END)
    return
second = float(format(5.30, '.2f'))
print (type(second))

def button_sub():
    global operation
    global f_number
    operation = "subs"
    f_number = float(e.get())
    e.delete(0,END)
    return

def button_mult ():
    global operation
    global f_number
    operation = "mult"
    f_number = float(e.get())
    e.delete(0,END)
    return

def button_div():
    global operation
    global f_number
    operation = "div"
    f_number = float(e.get())
    e.delete(0,END)
    return

def button_equal ():
    second = float(e.get())
    e.delete(0, END)

    if operation == "add" :
        sum = format ((f_number + second) , '.2f')
        e.insert(0, sum)
    elif operation == "mult" :
        multipl = format ((f_number * second) , '.2f')
        e.insert(0, multipl)
    elif operation == "div" :
        divide = f_number / second
        e.insert(0, format(divide ,'.2f'))
    elif operation == "subs" :
        sub = format ((f_number - second) , '.2f')
        e.insert(0, sub)
    else:
        e.insert(0, "You need to choose an operation , Try again")
        e.delete(0, END)

    return

button_1 = Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
button_0 = Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))

button_sub = Button(root,text="-",padx=38,pady=20,command= button_sub)
button_add = Button(root,text="+",padx=38,pady=20,command= button_add)
button_mult = Button(root,text="*",padx=38,pady=20,command= button_mult)
button_div = Button(root,text="/",padx=38,pady=20,command= button_div)
button_equal = Button(root,text="=",padx=91,pady=20,command= button_equal)
button_clear = Button(root,text="clear",padx=79,pady=20,command=lambda: button_click("clear"))


button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_sub.grid(row=6,column=0)
button_mult.grid(row=5,column=1)
button_div.grid(row=5,column=2)
button_equal.grid(row=6,column=1,columnspan=2)

root.mainloop()