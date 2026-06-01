# Day 27 - 100 Days of Code

from tkinter import *

print(f"\n---- Graphical ^ UI ----\n")

window = Tk()
window.title('Converter : Miles to Kilometres')
window.config(padx=20, pady=20)

def convert():
    mile = float(miles.get())
    kmetres = round(mile * 1.609)
    res.config(text=f'{kmetres}')

miles = Entry(width=5)
miles.grid(column=1, row=0)

label = Label(text='Miles')
label.grid(column=2, row=0)

equal = Label(text='equals')
equal.grid(column=0, row=1)

res = Label(text='0')
res.grid(column=1, row=1)

label_ = Label(text='Kilometres')
label_.grid(column=2, row=1)

button = Button(text='Calculate', command=convert)
button.grid(column=1, row=2)

window.mainloop()