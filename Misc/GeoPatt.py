from turtle import *

# Setup screen
bgcolor("black")
speed(0)
width(2)

colors = ["#FF1493", "#00BFFF", "#ADFF2F", "#FFD700"]

for i in range(120):
    pencolor( colors[i % 4] )
    
    # Petal - First half
    circle(i * 1.2, 180)
    right(45)
    
    # Petal - Second half
    circle(i * 1.2, 180)
    
    # Rotation to shift the next shape
    right(10)

done()