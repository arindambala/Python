from turtle import *
import colorsys

# Setup environment
bgcolor("black")
speed(0)
width(2)
tracer(5) # Skips frames for faster draw process

dist, rad = 0, 0 # Distance to move | Angle turn

penup()
goto(0, 200)
pendown()

while True:
    color = colorsys.hsv_to_rgb(rad / 210, 1.0, 1.0)
    pencolor(color)
    
    forward(dist)
    right(rad)
    
    dist += 3 ; rad += 1 # Outward spiral | Turn sharpness
    
    if (rad == 210):
        break
    
    hideturtle()

done()