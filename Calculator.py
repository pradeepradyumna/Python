from tkinter import *

root = Tk()
root.title("Pradeep's Calculator")

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def buttonClear_click():
    e.delete(0, END)


def buttonAdd_click():
    global firstnumber
    global math
    math = "add"
    firstnumber = int(e.get())
    e.delete(0, END)


def buttonSubtract_click():
    global firstnumber
    global math
    math = "sub"
    firstnumber = int(e.get())
    e.delete(0, END)


def buttonMultiply_click():
    global firstnumber
    #global math
    math = "mult"
    firstnumber = int(e.get())
    e.delete(0, END)


def buttonDivide_click():
    global firstnumber
    global math
    math = "div"
    firstnumber = int(e.get())
    e.delete(0, END)


def buttonEquals_click():
    current = e.get()
    e.delete(0, END)

    if math == "add":
        e.insert(0, int(current) + firstnumber)

    if math == "mult":
        e.insert(0, int(current) * firstnumber)

    if math == "div":
        e.insert(0, int(current) / firstnumber)

    if math == "sub":
        e.insert(0, int(current) - firstnumber)


btn1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
btn2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
btn3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
btn4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
btn5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
btn6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
btn7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
btn8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
btn9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
btn0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
btnAdd = Button(root, text="+", padx=40, pady=20, command=lambda: buttonAdd_click())
btnSubtract = Button(root, text="-", padx=40, pady=20, command=lambda: buttonSubtract_click())
btnMultiply = Button(root, text="*", padx=40, pady=20, command=lambda: buttonMultiply_click())
btnDivide = Button(root, text="/", padx=40, pady=20, command=lambda: buttonDivide_click())

btnEquals = Button(root, text="=", padx=40, pady=20, command=lambda: buttonEquals_click())
btnClear = Button(root, text="Clear", padx=40, pady=20, command=lambda: buttonClear_click())

btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)

btn0.grid(row=4, column=0)

btnClear.grid(row=5, column=0)
btnAdd.grid(row=5, column=1)
btnEquals.grid(row=5, column=2)

btnMultiply.grid(row=6, column=0)
btnDivide.grid(row=6, column=1)
btnSubtract.grid(row=6, column=2)

root.mainloop()
