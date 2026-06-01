# Day 27 - 100 Days of Code

import tkinter
from tkinter import END, IntVar

print(f"\n---- Graphical ^ UI ----\n")

window = tkinter.Tk()
window.title('Graphical UI')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Components
label = tkinter.Label(text='Watashi wa label desu :3', font=('Arial', 24, 'italic')) # Label Component
# label.pack(side='left', expand=True) # Packer
label.pack()

# label.config(text='Another One!') # label['text] = '_'

def button_onClick():
    print('I got clicked!')
    # label.config(text='Button got clicked!')
    # label.config(text=entry.get())
button = tkinter.Button(text='Click me!', command=button_onClick) # Button Component
button.place(x=100, y=75) # button.pack()

entry = tkinter.Entry(width=30) # Entry Component
entry.insert(END, string='Moshi Moshi! :3')
print(entry.get())
entry.pack() # entry.grid(row=3, column=5)

text = tkinter.Text(width=30, height=5) # Textbox Component
text.focus() # Cursor
text.insert(END, 'Multi-line Text Entry desu :P')
print(text.get('1.0', END)) # Returns current value in textbox at line 1, character 0
text.pack()

def box_used():
    print(spinbox.get()) # Returns the current spinbox value
spinbox = tkinter.Spinbox(from_=0, to=100, command=box_used) # Spinbox Component
spinbox.pack()

def scale_used(val): 
    print(val) # Current Scale Value
scale = tkinter.Scale(from_=0, to=100, command=scale_used) # Scale Component
scale.pack()

def check_used():
    print(check_state.get()) # Return 1 if ON button checked | 0
check_state = IntVar() # Holds checked state
checkBtn = tkinter.Checkbutton(text='Is ON?', variable=check_state, command=check_used) # CheckButton Component
check_state.get()
checkBtn.pack()

def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radioBtn1 = tkinter.Radiobutton(text='Option1', value=1, variable=radio_state, command=radio_used) # RadioButton Component
radioBtn2 = tkinter.Radiobutton(text='Option2', value=2, variable=radio_state, command=radio_used)
radioBtn1.pack()
radioBtn2.pack()

def listbox_used(event):
    print(listbox.get(listbox.curselection())) # Return current selection
listbox = tkinter.Listbox(height=5) # Listbox Component
fruits = ['Apple', 'Banana', 'Litchi', 'Mango', 'Watermelon']
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind('<<ListboxSelect>>', listbox_used)
listbox.pack()

'''
tkinter module acts as a wrapper (an interface) - Bridged to Tk (GUI Toolkit) from Tcl (Tool Command Language)

# *args

def add(a, b):
    return a + b
add(a=2, b=3)

def add(*args): # Unlimited Positional Arguments | Tuple | args[0]
    sum = 0
    for i in args:
        print(i) | sum += i
    return sum
print(add(2, 3, 5))

# **kwargs

def calc(n, **kwargs): # Unlimited Keyword Arguments | Dictionary | kwargs['key'] 
    for (key, value) in kwargs.items():
        n += kwargs['add']
        n *= kwargs['multiply]
        print(n)
calc(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.comp = kw['comp']
        self.mod = kw.get('mod') | Returns 'None' for unspecified keyword arguments

car = Car(comp='Nissan') // Car(mod='GT-R')
print(car.mod) | 'None'
'''

window.mainloop()