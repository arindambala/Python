from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
    
        self.shape('circle')
        self.speed('fastest')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
    
    def move_ball(self):
        pos_x = self.xcor() + self.x_move
        pos_y = self.ycor() + self.y_move
        self.goto(pos_x, pos_y)
    
    def bounce_ball(self):
        self.y_move *= -1