# Day 33 - 100 Days of Code

from tkinter import *
import requests

def get_quote():
    response = requests.get('https://aot-api.vercel.app/quote')
    response.raise_for_status()
    
    data = response.json()
    author = data['author']
    quote = data['quote']
    canvas.itemconfig(quote_text, text=quote)
    canvas.itemconfig(author_name, author)

window = Tk()
window.title('進撃の巨人')
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
bg_img = PhotoImage(file='background.png')
canvas.create_image(150, 207, image=bg_img)
quote_text = canvas.create_text(150, 207, text='心臓を捧げよ!', width=280, font=('Arial', 30, 'bold'), fill='black', justify='center')
author_name = canvas.create_text(150, 207, text='心臓を捧げよ!', width=280, font=('Arial', 30, 'bold'), fill='black', justify='center')
canvas.grid(row=0, column=0)

# ey_img = PhotoImage(file='eren.png')
# button = Button(image=ey_img, highlightthickness=0)
# button.grid(row=1, column=0)

window.mainloop()