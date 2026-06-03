# Day 28 - 100 dyas of Code

from tkinter import *

PINK = '#FFB5A7'
RED = '#E63946'
GREEN = '#A8DADC'
YELLOW = '#FFD166'
BG = '#F8F9FA'

FONT_NAME = 'Courier'
WORK = 25
SHORT_BREAK = 5
LONG_BREAK = 20

print(f"\n---- Pomodoro ^ Timer ----\n")

# -------- UI Setup --------
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50)

canvas = Canvas(width=200, height=224) # Canvas Widget
img = PhotoImage(file='tomato.png') # Holds an image at a file location
canvas.create_image(102, 112, image = img)
canvas.create_text(102, 130, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.pack()

window.mainloop()