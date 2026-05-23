from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class SnakeBody:
    def __init__(self):
        self.body = []
        self.create()
    
    def create(self):
        for part in POSITIONS: # Snake Body
            self.grow_body(part)
    
    def grow_body(self, part):
        parts = Turtle('square')
        parts.speed('fastest')
        parts.color('white')
        parts.penup()
        parts.goto(part)
        self.body.append(parts)
    
    def extend_body(self):
        self.grow_body(self.body[-1].position())