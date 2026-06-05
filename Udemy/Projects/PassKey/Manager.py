# Day 29 - 100 Days of Code

from tkinter import *

print(f"\n---- Password ^ Manager ----\n")

# -------- Key Generator --------

# -------- Save Password --------

# -------- UI Setup --------
window = Tk()
window.title("What's the key cuh?")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image = img)
canvas.pack()

window.mainloop()