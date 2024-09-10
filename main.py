import tkinter
from cProfile import label
from tkinter import *

#Function
def calculate():
    result = float(data_entry.get())
    result *= 1.609344.__round__(2)
    label_result.config(text=result)
    return result

#window
window = tkinter.Tk()
window.title("Mile to km Converter")
window.minsize(300, 150)

#labels
label_1 = Label (text = "is equal to", font = ("Arial",15))
label_1.grid(row = 1, column = 0)

label_miles = Label (text = "Miles", font = ("Arial",15))
label_miles.grid(row = 0, column = 2)

label_km = Label (text = "km", font = ("Arial",15))
label_km.grid(row = 1, column = 2)

label_result = Label (text = 0, font = ("Arial",15))
label_result ["text"] = 0
label_result.grid(row = 1, column = 1)

#Button
button_calculate = Button (text = "Calculate", font = ("Arial",15), command = calculate)
button_calculate.grid(row = 2, column = 1)

#Entry
data_entry = Entry(width = 20)
data_entry.grid(row = 0, column = 1)

window.mainloop()