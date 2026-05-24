from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        
        self.color('white')
        self.penup()
        self.hideturtle()
        
        self.left_player_score = 0
        self.right_player_score = 0
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_player_score, align='center', font=('Courier', 75, 'normal'))
        self.goto(100, 200)
        self.write(self.right_player_score, align='center', font=('Courier', 75, 'normal'))
    
    def left_player_point(self):
        self.left_player_score += 1
        self.update_score()
    
    def right_player_point(self):
        self.right_player_score += 1
        self.update_score()