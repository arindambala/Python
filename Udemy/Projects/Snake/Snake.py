# Day 20 - 100 Days of Code

from turtle import Screen
from Body import SnakeBody
from Move import SnakeMovement
import time

print(f"\n---- Turt ^ Race ----\n")

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake - 2D')
screen.tracer(0)

Snake = SnakeBody()
control = SnakeMovement(Snake.body)

# body = Turtle(shape='square')
# body.color('white')

# tail = Turtle('square')
# tail.color('white')
# tail.goto(-20, 0)

# head = Turtle('square')
# head.color('white')
# head.goto(-40, 0)

screen.listen()
screen.onkey(control.up, 'Up')
screen.onkey(control.down, 'Down')
screen.onkey(control.left, 'Left')
screen.onkey(control.right, 'Right')

play = True
while play:
    screen.update()
    time.sleep(0.1)
    
    control.move()

screen.exitonclick()