from tkinter import *

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


def normal_calculator_gui():
    global equation
    gui = Tk()
    gui.configure(background="Silver")
    gui.title("Simple Calculator")
    gui.geometry("360x480")
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation, font='Bold', borderwidth=10)
    expression_field.place(relx=0, rely=0, relheight=0.2, relwidth=1)
    button1 = Button(gui, text=' 1 ', font='Bold', fg='black', command=lambda: press(1), height=5, width=10)
    button1.place(relx=0, rely=0.2, relheight=0.16, relwidth=0.2)
    button2 = Button(gui, text=' 2 ', font='bold', fg='black', command=lambda: press(2), height=5, width=10)
    button2.place(relx=0.2, rely=0.2, relheight=0.16, relwidth=0.2)
    button3 = Button(gui, text=' 3 ', font='bold', fg='black', command=lambda: press(3), height=5, width=10)
    button3.place(relx=0.4, rely=0.2, relheight=0.16, relwidth=0.2)
    button4 = Button(gui, text=' 4 ', font='bold', fg='black', command=lambda: press(4), height=5, width=10)
    button4.place(relx=0, rely=0.36, relheight=0.16, relwidth=0.2)
    button5 = Button(gui, text=' 5 ', font='bold', fg='black', command=lambda: press(5), height=5, width=10)
    button5.place(relx=0.2, rely=0.36, relheight=0.16, relwidth=0.2)
    button6 = Button(gui, text=' 6 ', font='bold', fg='black', command=lambda: press(6), height=5, width=10)
    button6.place(relx=0.4, rely=0.36, relheight=0.16, relwidth=0.2)
    button7 = Button(gui, text=' 7 ', font='bold', fg='black', command=lambda: press(7), height=5, width=10)
    button7.place(relx=0, rely=0.52, relheight=0.16, relwidth=0.2)
    button8 = Button(gui, text=' 8 ', font='bold', fg='black', command=lambda: press(8), height=5, width=10)
    button8.place(relx=0.2, rely=0.52, relheight=0.16, relwidth=0.2)
    button9 = Button(gui, text=' 9 ', font='bold', fg='black', command=lambda: press(9), height=5, width=10)
    button9.place(relx=0.4, rely=0.52, relheight=0.16, relwidth=0.2)
    button0 = Button(gui, text=' 0 ', font='bold', fg='black', command=lambda: press(0), height=5, width=10)
    button0.place(relx=0, rely=0.68, relheight=0.16, relwidth=0.4)
    Decimal = Button(gui, text='.', font=('bold', 30), fg='black', command=lambda: press('.'), height=5, width=10)
    Decimal.place(relx=0.4, rely=0.68, relheight=0.16, relwidth=0.2)
    plus = Button(gui, text=' + ', font='bold', fg='black', command=lambda: press("+"), height=5, width=10)
    plus.place(relx=0.6, rely=0.2, relheight=0.16, relwidth=0.4)
    minus = Button(gui, text=' - ', font=('bold', 30), fg='black', command=lambda: press("-"), height=5, width=10)
    minus.place(relx=0.6, rely=0.36, relheight=0.16, relwidth=0.4)
    multiply = Button(gui, text=' * ', font=('bold',20), fg='black', command=lambda: press("*"), height=5, width=10)
    multiply.place(relx=0.6, rely=0.52, relheight=0.16, relwidth=0.4)
    divide = Button(gui, text=' / ', font='bold', fg='black', command=lambda: press("/"), height=5, width=10)
    divide.place(relx=0.6, rely=0.68, relheight=0.16, relwidth=0.4)
    equal = Button(gui, text=' = ', font='bold', fg='black', command=equalpress, height=5, width=10)
    equal.place(relx=0.4, rely=0.84, relheight=0.16, relwidth=0.6)
    clear_button = Button(gui, text='Clear', font='bold', fg='black', height=5, command=clear, width=10)
    clear_button.place(relx=0, rely=0.84, relheight=0.16, relwidth=0.4)
    gui.mainloop()
