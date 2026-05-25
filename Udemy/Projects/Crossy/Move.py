COLORS = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
START_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class Cars:
    def __init__(self):
        self.cars = []
        self.car_speed = START_MOVE_DISTANCE
    
    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            car = Turtle('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            
            pos_y = random.randint(-250, 250)
            car.goto(300, pos_y)
            self.cars.append(car)
    
    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT