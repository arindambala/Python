# Day 29 - 100 Days of Code

from tkinter import *

print(f"\n---- Password ^ Manager ----\n")

# -------- Key Generator --------

# -------- Save Password --------
def saveTo():
    website = web.get()
    mail = user.get()
    key = hole.get()
    
    with open('data.txt', 'a') as file:
        file.write(f'{website} | {mail} | {key}\n')
        web.delete(0, END)
        hole.delete(0, END)

# -------- UI Setup --------
window = Tk()
window.title("What's the key cuh?")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image = img)
canvas.grid(row=0, column=1) # canvas.pack()

website = Label(text='Website :')
website.grid(row=1, column=0)
mail = Label(text='Email/Username :')
mail.grid(row=2, column=0)
key = Label(text='Password :')
key.grid(row=3, column=0)

web = Entry(width=35)
web.grid(row=1, column=1, columnspan=2)
web.focus() # Cursor on the data entry
user = Entry(width=35)
user.grid(row=2, column=1, columnspan=2)
user.insert(0, 'username@email.domain')
hole = Entry(width=21)
hole.grid(row=3, column=1)

generate = Button(text='Generate Password')
generate.grid(row=3, column=2)
add = Button(text='Add', width=36, command=saveTo)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()