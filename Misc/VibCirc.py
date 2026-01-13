from turtle import *

# Setup environment
bgcolor("black")
pencolor("white")
speed(0)

dist, rad = 0 , 0 # Distance to move | Angle turn

penup()
goto(0, 200)
pendown()

while True:
    forward(dist)
    right(rad)
    
    dist += 3 ; rad += 1 # Outward spiral | Turn sharpness
    
    if (rad == 210):
        break
    
    hideturtle()

done()