from tkinter import *

win = Tk()

def dote():
    screen.insert(END, '.')

def delet():
    screen.delete(0, END)

def zero():
    screen.insert(END, 0)

def one():
    screen.insert(END, 1)

def two():
    screen.insert(END, 2)

def three():
    screen.insert(END, 3)

def four():
    screen.insert(END, 4)

def five():
    screen.insert(END, 5)

def six():
    screen.insert(END, 6)

def seven():
    screen.insert(END, 7)

def eight():
    screen.insert(END, 8)

def nine():
    screen.insert(END, 9)

def add():
        screen.insert(END, '+')

def sub():
    screen.insert(END, '-')

def mult():
    screen.insert(END, '*')

def div():
    screen.insert(END, '/')

def lpar():
    screen.insert(END, '(')

def rpar():
    screen.insert(END, ')')

def neg():
    screen.insert(END, '-')

def calcul():
    try:
        ans = eval(screen.get())
        screen.delete(0,END)
        screen.insert(END, ans)
    except ZeroDivisionError as z:
        screen.delete(0, END)
        screen.insert(END, ('Invalid Input',z))

screen = Entry(win, width = 24, font = ('Arial',10))
screen.grid(row = 0, column = 0, columnspan = 4)

dote_b = Button(win, text = ".", command = dote, height = 3, width = 3)
dote_b.grid(row = 5, column = 0)

zero_b = Button(win, text = "0", command = zero, height = 3, width = 3)
zero_b.grid(row = 5, column = 1)

negativ_b = Button(win, text = "+-", command = neg, height = 3, width = 3)
negativ_b.grid(row = 5, column = 2)

one_b = Button(win, text = "1", command = one, height = 3, width = 3)
one_b.grid(row = 4, column = 0)

two_b = Button(win, text = "2", command = two, height = 3, width = 3)
two_b.grid(row = 4, column = 1)

three_b = Button(win, text = "3", command = three, height = 3, width = 3)
three_b.grid(row = 4, column = 2)

four_b = Button(win, text = "4", command = four, height = 3, width = 3)
four_b.grid(row = 3, column = 0)

five_b = Button(win, text = "5", command = five, height = 3, width = 3)
five_b.grid(row = 3, column = 1)

six_b = Button(win, text = "6", command = six, height = 3, width = 3)
six_b.grid(row = 3, column = 2)

seven_b = Button(win, text = "7", command = seven, height = 3, width = 3)
seven_b.grid(row = 2, column = 0)

eight_b = Button(win, text = "8", command = eight, height = 3, width = 3)
eight_b.grid(row = 2, column = 1)

nine_b = Button(win, text = "9", command = nine, height = 3, width = 3)
nine_b.grid(row = 2, column = 2)

equal_b = Button(win, text = "=", command = calcul, height = 3, width = 3)
equal_b.grid(row = 5, column = 3)

plus_b = Button(win, text = "+", command = add, height = 3, width = 3)
plus_b.grid(row = 4, column = 3)

minus_b = Button(win, text = "-", command = sub, height = 3, width = 3)
minus_b.grid(row = 3, column = 3)

mult_b = Button(win, text = "*", command = mult, height = 3, width = 3)
mult_b.grid(row = 2, column = 3)

div_b = Button(win, text = "/", command = div, height = 3, width = 3)
div_b.grid(row = 1, column = 3)

delete_b = Button(win, text = "➡️", command = delet, height = 3, width = 3)
delete_b.grid(row = 1, column = 2)

rpar_b = Button(win, text = ")", command = rpar, height = 3, width = 3)
rpar_b.grid(row = 1,column = 1)

lpar_b = Button(win, text = "(", command = lpar, height = 3, width = 3)
lpar_b.grid(row = 1, column = 0)


win.mainloop()