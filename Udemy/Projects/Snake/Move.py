MOVE_DISTANCE = 20

RIGHT, UP, LEFT, DOWN = 0, 90, 180, 270

class SnakeMovement:
    def __init__(self, body):
        self.body = body
        self.head = body[0]
    
    def move(self):
        for limb in range(len(self.body) - 1, 0, -1): # range(start, stop, step) | range(2, 0, -1)
            # limb.forward(20)
            cor_x = self.body[limb - 1].xcor()
            cor_y = self.body[limb - 1].ycor()
            self.body[limb].goto(cor_x, cor_y) # Snake Movement
        self.head.forward(MOVE_DISTANCE)
        # body[0].left(90)
    
    def refer_body(self, build):
        self.body = build
        self.head  = build[0]
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)