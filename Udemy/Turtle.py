# Day 18 - 100 Days of Code

from turtle import Turtle, Screen
import random

bloom = Turtle()
bloom.shape('turtle')
bloom.color('DarkOrchid')

# bloom.forward(100) # Distance
# bloom.right(90) # Angle

# # Square
# for _ in range(4):
#     bloom.forward(100)
#     bloom.right(90)

# # Dashed Line
# for _ in range(10):
#     bloom.forward(10)
#     bloom.penup()
#     bloom.forward(10)
#     bloom.pendown()

# # Shapes
colors = [
    "DarkOrchid", "Crimson", "Gold", "LimeGreen", "DeepSkyBlue", "Chocolate", "HotPink", "SlateGray", "MediumPurple", "OrangeRed"
]

# for sides in range(3, 11):
#     bloom.pencolor(random.choice(colors))
#     for _ in range(sides):
#         angle = 360 / sides
#         bloom.forward(100)
#         bloom.right(angle)

# Walk
directions = [0, 90, 180, 270]

for _ in range(200):
    bloom.color(random.choice(colors))
    bloom.forward(25)
    bloom.setheading(random.choice(directions))
    
screen = Screen()
screen.exitonclick()