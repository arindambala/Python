# Day 31 - 100 Days of Code

RED = '#DE1A24'
GREEN = '#23C552'
BG_COLOR = '#B1DDC6'
FG_COLOR = '#E5E5EA'

from tkinter import *

print(f"\n ---- Flash ^ Cards ---- \n")

window = Tk()
window.title("Vive l'Angleterre - Vive la France")
window.config(padx=50, pady=50, bg=BG_COLOR)

canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
cf_img = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image = cf_img)
canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
canvas.create_text(400, 263, text='word', font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

wrg_img = PhotoImage(file='images/wrong.png')
unknown_Button = Button(image=wrg_img)
unknown_Button.grid(row=1, column=0)

rgt_img = PhotoImage(file='images/right.png')
known_Button = Button(image=rgt_img)
known_Button.grid(row=1, column=1)

window.mainloop()