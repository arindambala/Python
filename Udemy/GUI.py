# Day 27 - 100 Days of Code

import tkinter

print(f"\n---- Graphical ^ UI ----\n")

window = tkinter.Tk()
window.title('Graphical UI')
window.minsize(width=500, height=300)

# Components
label = tkinter.Label(text='Watashi wa label desu :3', font=('Arial', 24, 'italic')) # Label
label.pack(side='left', expand=True) # Packer

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