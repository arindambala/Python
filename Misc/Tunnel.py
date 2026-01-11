import turtle
import colorsys

# Setup environment
turt = turtle.Turtle()
scr = turtle.Screen()
turt.speed(0)
turt.width(2)
scr.bgcolor("black")

# Loop to create squares
for i in range(200):
    # Colour change for rainbow effect
    color = colorsys.hsv_to_rgb(i / 200, 1.0, 1.0)
    turt.pencolor(color)

    # Loop to complete the square
    for _ in range(4):
        turt.forward(i * 2)
        turt.left(90)

    # Turn for spiral illusion
    turt.left(5)

turtle.done()