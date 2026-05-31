# Day 27 - 100 Days of Code

import tkinter

print(f"\n---- Graphical ^ UI ----\n")

window = tkinter.Tk()
window.title('Graphical UI')
window.minsize(width=500, height=300)

# Components
label = tkinter.Label(text='Watashi wa label desu :3', font=('Arial', 24, 'italic')) # Label
label.pack()

window.mainloop()