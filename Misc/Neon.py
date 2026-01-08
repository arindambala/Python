import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Geometric Neon Flower")

#Turtle setup
t = turtle.Turtle()
t.speed(0) # Fastest
t.width(2)

# Colour generation
n = 36 # Shapes
for i in range(200):
    # Rainbow effect cycle through hue spectrum
    colour = colorsys.hsv_to_rgb(i / 200, 1.0, 1.0)
    t.pencolor(colour)
    
    # Pattern
    t.forward(i * 1.5)
    t.left(59) # Spiral angle
    t.forward(i * 0.5)
    t.right(120) # Sharp edges
    
turtle.done()