# Day 21 - 100 Days of Code

ALIGNMENT = 'center'
FONT = ('Courier', 19, 'bold')

from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        
        self.score = 0
        with open('Data.txt') as file:
            self.high_score = int(file.read()) # Read
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} | High Score : {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def reset_score(self):
        self.final_score = self.score
        
        if self.score > self.high_score:
            self.high_score = self.score
            with open('Data.txt', mode = 'w') as file:
                file.write(f"{self.high_score}") # Write
        self.score = 0
    
    def detect_wall(self):
        self.clear()
        self.goto(0, 20)
        self.write('GAME OVER !!', align=ALIGNMENT, font=FONT)
        self.goto(0, -20)
        self.write(f"Final Score : {self.final_score}", align=ALIGNMENT, font=FONT)
    
    def count_score(self):
        self.score += 1
        self.update_score()