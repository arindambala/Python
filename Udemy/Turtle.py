# Day 18 - 100 Days of Code

from turtle import Turtle, Screen

bloom = Turtle()
bloom.shape('turtle')
bloom.color('DarkOrchid')

# bloom.forward(100) # Distance
# bloom.right(90) # Angle

# # Square
# for _ in range(4):
#     bloom.forward(100)
#     bloom.right(90)

# Dashed Line
for _ in range(10):
    bloom.forward(10)
    bloom.penup()
    bloom.forward(10)
    bloom.pendown()

screen = Screen()
screen.exitonclick()