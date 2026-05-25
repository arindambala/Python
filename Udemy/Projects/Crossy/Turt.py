START_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.speed('fastest')
        self.color('DarkOrchid')
        self.penup()
        self.road_start()
        self.setheading(90)
    
    def move_play(self):
        self.forward(MOVE_DISTANCE)
    
    def road_start(self):
        self.goto(START_POSITION)

    def road_end(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False