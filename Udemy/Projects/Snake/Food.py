# Day 21 - 100 Days of Code

from turtle import Turtle
import random

class SnakeFood(Turtle): # Inheritance
    def __init__(self):
        super().__init__()
        
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('purple')
        self.speed('fastest')
        self.refresh()
    
    def refresh(self):
        food_pos_x = random.randint(-280, 280)
        food_pos_y = random.randint(-280, 280)
        
        self.goto(food_pos_x, food_pos_y)