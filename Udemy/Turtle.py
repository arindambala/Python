# Day 18 - 100 Days of Code

from turtle import Turtle, Screen
import turtle
import random

bloom = Turtle()
bloom.shape('turtle')
bloom.color('DarkOrchid')
turtle.colormode(255)

bloom.forward(100) # Distance
bloom.right(90) # Angle

# Square
for _ in range(4):
    bloom.forward(100)
    bloom.right(90)

# Dashed Line
for _ in range(10):
    bloom.forward(10)
    bloom.penup()
    bloom.forward(10)
    bloom.pendown()

# Shapes
colors = [
    "DarkOrchid", "Crimson", "Gold", "LimeGreen", "DeepSkyBlue", "Chocolate", "HotPink", "SlateGray", "MediumPurple", "OrangeRed"
]

for sides in range(3, 11):
    bloom.pencolor(random.choice(colors))
    for _ in range(sides):
        angle = 360 / sides
        bloom.forward(100)
        bloom.right(angle)

# Walk
directions = [0, 90, 180, 270]
bloom.pensize(15)
bloom.speed('fastest')

for _ in range(200):
    bloom.color(random.choice(colors))
    bloom.forward(25)
    bloom.setheading(random.choice(directions))

# Spirograph
def color_gen():
    r, g, b = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )
    random_colors = (r, g, b)
    return random_colors

bloom.speed('fastest')
gap = 5 

for _ in range(int(360 / gap)):
    bloom.color(color_gen())
    bloom.circle(100)
    bloom.setheading(bloom.heading() + gap)

screen = Screen()
screen.exitonclick()