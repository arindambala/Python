# Day 19 - 100 Days of Code

from turtle import Turtle, Screen

bloom = Turtle()
screen = Screen()
bloom.speed('fastest')

def move_forward():
    bloom.forward(10)
def move_backward():
    bloom.backward(10)
def move_left():
    # turn = bloom.heading() + 10
    # bloom.setheading(turn)
    bloom.left(10)
def move_right():
    # turn = bloom.heading() - 10
    # bloom.setheading(turn)
    bloom.right(10)
def clean():
    bloom.clear()
    bloom.penup()
    bloom.home()
    bloom.pendown()

screen.listen()

screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(move_left, 'a')
screen.onkey(move_right, 'd')
screen.onkey(clean, 'c')

screen.exitonclick()