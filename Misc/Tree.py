from turtle import *

# Setup environment
setup(800, 600)
bgcolor("black")
color("lime")
speed(0)
width(2)

penup()
goto(0, -250)
pendown()
left(90) # Turtle points upwards

def tree(br_len):
    if br_len > 5: # Stops when branches are too small
        forward(br_len) # Main branch
        
        right(20)
        tree(br_len - 15) # Smaller sub-tree
        
        left(40)
        tree(br_len - 15) # Another smaller sub-tree
        
        right(20)
        backward(br_len) # Restore branch

tree(80)
hideturtle()
done()