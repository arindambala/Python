from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        
        self.shape('square')
        self.speed('fastest')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(pos)

    def move_paddle_up(self):
        pos_y = self.ycor() + 20
        if self.ycor() < 250:
            self.goto(self.xcor(), pos_y)

    def move_paddle_down(self):
        pos_y = self.ycor() - 20
        if self.ycor() > -250:
            self.goto(self.xcor(), pos_y)