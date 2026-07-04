THEME_COLOUR = '#253A45'

from tkinter import *
from Func import Task

class Interface:
    def __init__(self, func: Task):
        self.quiz = func
        
        self.window = Tk()
        self.window.title('Factos')
        self.window.config(padx=20, pady=20, bg=THEME_COLOUR)
        
        self.score = Label(text='Score: 0', fg='white', bg=THEME_COLOUR)
        self.score.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.ques_text = self.canvas.create_text(150, 125, width=280, text='Some Text', fill=THEME_COLOUR, font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        self.true_img = PhotoImage(file='images/true.png')
        self.true_button = Button(image=self.true_img, highlightthickness=0, bd=0, bg=THEME_COLOUR, activebackground=THEME_COLOUR)
        self.true_button.grid(row=2, column=0)
        
        self.false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=self.false_img, highlightthickness=0, bd=0, bg=THEME_COLOUR, activebackground=THEME_COLOUR)
        self.false_button.grid(row=2, column=1)
        
        self.get_next_ques()
        
        self.window.mainloop()
    
    def get_next_ques(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.ques_text, text=q_text)