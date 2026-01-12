from turtle import *

# Set the colour
color('red', 'yellow')
shape('classic')

begin_fill()
while True:
    forward(200)
    left(170)
    
    # Break point
    if abs(pos()) < 1:
        break

end_fill()
done()