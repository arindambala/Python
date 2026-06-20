# Day 31 - 100 Days of Code

BG_COLOR = '#B1DDC6'

from tkinter import *
import pandas
import random

print(f"\n ---- Flash ^ Cards ---- \n")

df = pandas.read_csv('data/french_words.csv')
# print(df)
learn = df.to_dict(orient='records') # Orients the table to create the dictionary
curr_card = {}

def nxt_card():
    global curr_card, flip_timer
    window.after_cancel(flip_timer)
    
    curr_card = random.choice(learn)
    # print(curr_card['French'])
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=curr_card['French'], fill='black')
    canvas.itemconfig(card_background, image=cf_img)
    
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=curr_card['English'], fill='white')
    canvas.itemconfig(card_background, image=cb_img)

window = Tk()
window.title("Vive l'Angleterre - Vive la France")
window.config(padx=50, pady=50, bg=BG_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
cf_img = PhotoImage(file='images/card_front.png')
cb_img = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image = cf_img)
card_title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='word', font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

wrg_img = PhotoImage(file='images/wrong.png')
unknown_Button = Button(image=wrg_img, highlightthickness=0, command=nxt_card)
unknown_Button.grid(row=1, column=0)

rgt_img = PhotoImage(file='images/right.png')
known_Button = Button(image=rgt_img, highlightthickness=0, command=nxt_card)
known_Button.grid(row=1, column=1)

nxt_card()

window.mainloop()