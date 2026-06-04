# Day 28 - 100 dyas of Code

from tkinter import *

PINK = '#FFB5A7'
RED = '#E63946'
GREEN = '#1E4B27'
YELLOW = '#FFD166'

FONT_NAME = 'Courier'
WORK = 25
SHORT_BREAK = 5
LONG_BREAK = 20

print(f"\n---- Pomodoro ^ Timer ----\n")

# -------- UI Setup --------
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text='TIMER', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, 'bold italic'))
title.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # Canvas Widget
img = PhotoImage(file='tomato.png') # Holds an image at a file location
canvas.create_image(100, 112, image = img)
canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(row=1, column=1) # canvas.pack()

start = Button(text='Start', font=(FONT_NAME, 10, 'italic'), highlightthickness=0)
start.grid(row=2, column=0)

reset = Button(text='Reset', font=(FONT_NAME, 10, 'italic'), highlightthickness=0)
reset.grid(row=2, column=2)

window.mainloop()