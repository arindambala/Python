# Day 21 - 100 Days of Code

ALIGNMENT = 'center'
FONT = ('Courier', 19, 'bold')

from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)
    
    def detect_wall(self):
        self.goto(0, 0)
        self.write('GAME OVER !!', align=ALIGNMENT, font=FONT)
    
    # def detect_tail(self):
    
    def count_score(self):
        self.score += 1
        self.clear()
        self.update_score()