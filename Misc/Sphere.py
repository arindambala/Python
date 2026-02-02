from turtle import *
import math

# Setup environment
speed(0)
width(2)
bgcolor('white')

# Pattern
color('magenta') # color('blue')
penup()
goto(0, 0) # goto(-200, 0)
pendown()

petals = 18
petals_radius = 120

for _ in range(petals): # for _ in range(12):
    circle(petals_radius) # circle(60)
    left(360 / petals) # left(30)

# penup()
# goto(150, -60)
# setheading(0)
# pendown()
# color('darkgreen')

color('green') # color('gold')
radius = 80

for i in range(-radius, radius, 6): # 5
    rad = math.sqrt(radius ** 2 - i ** 2)
    penup()
    goto(-rad, i) # goto(150 - rad, i)
    pendown()
    circle(rad)

color('orange')
for _ in range(24):
    circle(40)
    left(15)

# hideturtle()
done()