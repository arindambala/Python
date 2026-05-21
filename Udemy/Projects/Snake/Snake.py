# Day 20 - 100 Days of Code

from turtle import Turtle, Screen
import time

print(f"\n---- Turt ^ Race ----\n")

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake - 2D')
screen.tracer(0)

pos = [(0, 0), (-20, 0), (-40, 0)]
body = []

# body = Turtle(shape='square')
# body.color('white')

# tail = Turtle('square')
# tail.color('white')
# tail.goto(-20, 0)

# head = Turtle('square')
# head.color('white')
# head.goto(-40, 0)

for part in pos: # Snake Body
    parts = Turtle('square')
    parts.color('white')
    parts.penup()
    parts.goto(part)
    body.append(parts)


play = True
while play:
    screen.update()
    time.sleep(0.1)
    
    for limb in range(len(body) - 1, 0, -1): # range(start, stop, step) | range(2, 0, -1)
        # limb.forward(20)
        cor_x = body[limb - 1].xcor()
        cor_y = body[limb - 1].ycor()
        body[limb].goto(cor_x, cor_y) # Snake Movement
    body[0].forward(20)
    # body[0].left(90)

screen.exitonclick()