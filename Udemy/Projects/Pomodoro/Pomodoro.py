# Day 28 - 100 dyas of Code

from tkinter import *
import math

PINK = '#FFB5A7'
RED = '#E63946'
GREEN = '#1E4B27'
YELLOW = '#FFD166'

FONT_NAME = 'Courier'
WORK = 25
SHORT_BREAK = 5
LONG_BREAK = 20

REPS = 0
TIME = NONE

print(f"\n---- Pomodoro ^ Timer ----\n")

# -------- Reset Mechanism --------
def reset_timer():
    window.after_cancel(TIME)
    canvas.itemconfig(timer, text='00:00', font=(FONT_NAME, 30, 'bold'))
    title.config(text='TIMER', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, 'bold italic'))
    ticks.config(text='')
    
    global REPS
    REPS = 0

# -------- Timer Mechanism --------
def start_timer():
    global REPS
    REPS += 1
    
    work = WORK * 60
    short_break = SHORT_BREAK * 60
    long_break = LONG_BREAK * 60
    
    if REPS % 8 == 0:
        counter(long_break)
        title.config(text='Break!', fg=RED, font=(FONT_NAME, 25, 'italic'))
    elif REPS % 2 == 0:
        counter(short_break)
        title.config(text='Break!', fg=PINK, font=(FONT_NAME, 25, 'italic'))
    else:
        counter(work)
        title.config(text='Work!', fg=GREEN, font=(FONT_NAME, 25, 'italic'))

# -------- Countdown Mechanism --------
def counter(count):
    mins = int(math.floor(count / 60))
    secs = count % 60
    
    if secs < 10:
        secs = f'0{secs}' # Dynamic Typing
    
    canvas.itemconfig(timer, text=f'{mins}:{secs}') # Changes properties of specific element
    if count > 0:
        global TIME
        TIME = window.after(1000, counter, count - 1) # Delays execution without freezing the interface
    else:
        start_timer()
        marks = ''
        session = math.floor(REPS / 2)
        for _ in range(session):
            marks += '✅'
        ticks.config(text=marks)

# -------- UI Setup --------
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text='TIMER', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, 'bold italic'))
title.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # Canvas Widget
img = PhotoImage(file='tomato.png') # Holds an image at a file location
canvas.create_image(100, 112, image = img)
timer = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(row=1, column=1) # canvas.pack()

start = Button(text='Start', font=(FONT_NAME, 10, 'italic'), highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text='Reset', font=(FONT_NAME, 10, 'italic'), highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)

ticks = Label(fg=GREEN, bg=YELLOW)
ticks.grid(row=3, column=1)

window.mainloop()