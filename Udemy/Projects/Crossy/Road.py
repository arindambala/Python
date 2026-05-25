# Day 23 - 100 Days of Code

from turtle import Screen
from Turt import Player
from Move import Cars
from Score import ScoreBoard
import time

print(f"\n ---- Crossy ^ Road ---- \n")

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turt = Player()
car = Cars()

screen.listen()
screen.onkey(turt.move_play, 'Up')

play = True
while play:
    time.sleep(0.1)
    screen.update()
    
    car.create_car()
    car.move_cars()
    
    for one_car in car.cars: # Collision
        if one_car.distance(turt) < 20:
            play = False

screen.exitonclick()