from turtle import *

# Setup environment
speed(0)
bgcolor('black')
color('greenyellow')
pensize(5)

for i in range(8):
    left(45)
    for i in range(8):
        forward(100)
        right(45)

done()