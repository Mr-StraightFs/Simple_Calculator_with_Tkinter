import tkinter
from tkinter import *

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.entry = Entry(self.root, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        self.buttons = [
            ("1", lambda: self.button_click(1)),
            ("2", lambda: self.button_click(2)),
            ("3", lambda: self.button_click(3)),
            ("4", lambda: self.button_click(4)),
            ("5", lambda: self.button_click(5)),
            ("6", lambda: self.button_click(6)),
            ("7", lambda: self.button_click(7)),
            ("8", lambda: self.button_click(8)),
            ("9", lambda: self.button_click(9)),
            ("0", lambda: self.button_click(0)),
            ("-", self.button_sub),
            ("+", self.button_add),
            ("*", self.button_mult),
            ("/", self.button_div),
            ("=", self.button_equal),
            ("clear", lambda: self.button_click("clear"))
        ]

        for i, (text, command) in enumerate(self.buttons):
            button = Button(self.root, text=text, padx=40, pady=20, command=command)
            button.grid(row=i // 3 + 1, column=i % 3)

    def button_click(self, number):
        if number == "clear":
            self.entry.delete(0, END)
            return
        current = self.entry.get()
        self.entry.delete(0, END)
        self.entry.insert(0, str(current) + str(number))

    def button_add(self):
        self.operation = "add"
        self.f_number = float(self.entry.get())
        self.entry.delete(0, END)

    def button_sub(self):
        self.operation = "subs"
        self.f_number = float(self.entry.get())
        self.entry.delete(0, END)

    def button_mult(self):
        self.operation = "mult"
        self.f_number = float(self.entry.get())
        self.entry.delete(0, END)

    def button_div(self):
        self.operation = "div"
        self.f_number = float(self.entry.get())
        self.entry.delete(0, END)

    def button_equal(self):
        try:
            second = float(self.entry.get())
            self.entry.delete(0, END)
            if self.operation == "add":
                sum = format((self.f_number + second), '.2f')
                self.entry.insert(0, sum)
            elif self.operation == "mult":
                multipl = format((self.f_number * second), '.2f')
                self.entry.insert(0, multipl)
            elif self.operation == "div":
                divide = self.f_number / second
                self.entry.insert(0, format(divide, '.2f'))
            else:
                sub = format((self.f_number - second), '.2f')
                self.entry.insert(0, sub)
        except Exception as e:
            self.entry.insert(0, "Choose a correct operation, Try again")

if __name__ == "__main__":
    root = Tk()
    app = SimpleCalculator(root)
    root.mainloop()
