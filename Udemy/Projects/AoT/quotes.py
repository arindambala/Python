# Day 33 - 100 Days of Code

from tkinter import *
import requests

def get_quote():
    response = requests.get('https://aot-api.vercel.app/quote')
    response.raise_for_status()
    
    data = response.json()
    author = data['author']
    quote = data['quote']
    canvas.itemconfig(quote_text, text=f'{quote}')
    
    quote_bounds = canvas.bbox(quote_text)
    quote_bottom = quote_bounds[3]
    
    canvas.coords(author_name, 150, quote_bottom + 20)
    canvas.itemconfig(author_name, text=f'- {author}')

window = Tk()
window.title('進撃の巨人')
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
bg_img = PhotoImage(file='background.png')
canvas.create_image(150, 207, image=bg_img)

quote_text = canvas.create_text(150, 100, text='心臓を捧げよ!', width=280, font=('Arial', 16, 'bold'), fill='black', justify='center', anchor='n')
author_name = canvas.create_text(150, 150, text='', width=280, font=('Arial', 12, 'bold italic'), fill='black', justify='center', anchor='n')
canvas.grid(row=0, column=0)

# ey_img = PhotoImage(file='eren.png')
# button = Button(image=ey_img, highlightthickness=0)
# button.grid(row=1, column=0)

button = Button(text='Next', font=('Arial', 12, 'bold'), command=get_quote)
button.grid(row=1, column=0, pady=20)

window.mainloop()