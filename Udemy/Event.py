# Day 19 - 100 Days Of Code

from turtle import Turtle, Screen

# Event Listeners
bloom = Turtle()
screen = Screen()

def move_forward():
    bloom.forward(10)

screen.listen()
screen.onkey(key='space', fun=move_forward) # High Order Functions
screen.exitonclick()