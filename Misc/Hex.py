from turtle import *
import colorsys
import math

# Setup environment
bgcolor("black")
title("Hexagonal Kaleidoscope")
speed(0)
width(2)
# hideturtle()
# tracer(0, 0)

# Draw a hexagon
def draw_hex(size):
    for _ in range(6):
        forward(size)
        left(60)

# Main pattern
hex = 300 # 180
base_size = 10 # 20
rotation = 11 # 7 # Degrees between hexagons
radius_growth = 1.5 # 3 # Spiral expansion

for i in range(hex):
    hue = i / hex
    (r, g, b) = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    pencolor(r,g ,b)
    
    # Move outward spiral
    angle = math.radians(i * rotation)
    radius = i * radius_growth
    
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    
    penup()
    goto(x, y)
    setheading(i * rotation)
    pendown()
    
    draw_hex(base_size + i * 0.2)

update()
done()