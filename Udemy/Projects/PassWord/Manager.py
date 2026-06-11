# Day 29 - 100 Days of Code

from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

print(f"\n---- Password ^ Manager ----\n")

# -------- Key Generator --------
def createPw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [choice(letters) for _ in range(randint(8, 10))]
    pw_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    pw_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    pw_list = pw_letters + pw_numbers + pw_symbols
    shuffle(pw_list)

    password = "".join(pw_list)
    hole.insert(0, password)
    
    pyperclip.copy(password) # Clipboard

# -------- Save Password --------
def saveTo():
    website = web.get()
    mail = user.get()
    key = hole.get()
    
    data = {
        website: {
            'email': mail,
            'password': key,
        }
    }
    
    if len(website) == 0 or len(key) == 0:
        messagebox.showerror(title='INVALID!', message='Empty fields are not allowed.')
    else:
        # choice = messagebox.askokcancel(title=website, message=f'Details provided: \nEmail: {mail} \nPassword: {key} \nTo be saved?')
        # if choice:
        with open('data.json', 'r') as file: # with open('data.txt', 'a') as file:
            # json.dump(data, file, indent=4) # file.write(f'{website} | {mail} | {key}\n')
            file_data = json.load(file) # print(data)
            file_data.update(data)
        
        with open('data.json', 'w') as file:    
            json.dump(file_data, file, indent=4)
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

generate = Button(text='Generate Password', command=createPw)
generate.grid(row=3, column=2)
add = Button(text='Add', width=36, command=saveTo)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()