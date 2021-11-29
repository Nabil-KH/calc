from tkinter import Tk, Label, Button,StringVar, Entry,Text, END

win = Tk()
b = Button

def BMI():
    
    weight = float(weight_value.get())
    height = float(height_value.get())
    bmi = weight / height**2
    if bmi < 18.5 :
        res = "Underweight"
     
    elif bmi >= 18.5 and bmi < 25 :
        res = "Normal"
    
    elif bmi >= 25 and bmi < 30 :
        res = "Overweight"
        
    elif bmi >= 30:
            res = "Obesity"
    
    _bmi.delete('1.0', END)
    _bmi.insert(END,bmi)
   
    _result.delete('1.0', END)
    _result.insert(END,res)
    
    _done.delete('1.0',END)
    _done.insert(END, ' ')
def done():
     
     _done.delete('1.0', END)
     _done.insert(END, 'Good Bay')
     
title = Label(win, text = 'BMI Calculation')

weight = Label(win, text = 'Enter your weight')
weight_value = StringVar()
wght = Entry(win, textvariable = weight_value)
weight_unit = Label(win, text = 'kg')

height = Label(win, text =  'Enter your height')
height_value = StringVar()
hght = Entry(win, textvariable = height_value)
height_unit = Label(win, text = 'm')

bmi_value = Label(win, text = 'Your BMI is')
_bmi = Text(win, height = 1, width = 21)
bmi_unit = Label(win, text = 'kg/m^2')

result = Label(win, text = 'RESULT')
_result = Text(win, height = 1, width = 21)

_done = Text(win, height = 1, width =21)
b1 = b(win, text = 'CALCULAT', command = BMI, bg = 'green')
b2 = b(win, text = 'DONE', command = done, bg = 'blue')

title.grid(row = 0, column = 1)

weight.grid(row = 1, column = 0)
wght.grid(row = 1, column = 1)
weight_unit.grid(row = 1, column = 2)

height.grid(row = 2, column = 0)
hght.grid(row= 2, column = 1)
height_unit.grid(row = 2, column = 2)

bmi_value.grid(row = 3, column = 0)
_bmi.grid(row = 3, column = 1)
bmi_unit.grid (row = 3, column = 2)

result.grid(row = 4, column = 0)
_result.grid(row = 4, column = 1)

_done.grid(row =5, column = 1)
b1.grid(row = 6, column = 0)
b2.grid(row = 6, column = 2)

win.mainloop()