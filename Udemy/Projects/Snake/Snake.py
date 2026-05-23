# Day 20 - 100 Days of Code

from turtle import Screen
from Body import SnakeBody
from Move import SnakeMovement
from Food import SnakeFood
from Score import ScoreBoard
import time

print(f"\n---- Snake ^ 2D ----\n")

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake - 2D')
screen.tracer(0)

Snake = SnakeBody()
Control = SnakeMovement(Snake.body)
Food = SnakeFood()
Board = ScoreBoard()

# body = Turtle(shape='square')
# body.color('white')

# tail = Turtle('square')
# tail.color('white')
# tail.goto(-20, 0)

# head = Turtle('square')
# head.color('white')
# head.goto(-40, 0)

screen.listen()
screen.onkey(Control.up, 'Up')
screen.onkey(Control.down, 'Down')
screen.onkey(Control.left, 'Left')
screen.onkey(Control.right, 'Right')

play = True
while play:
    screen.update()
    time.sleep(0.1)
    
    Control.move()
    
    if Control.head.distance(Food) < 15: # Snake.body[0]
        # print("NomNomNom")
        Food.refresh()
        Snake.extend_body()
        Board.count_score()
    
    if Control.head.xcor() > 280 or Control.head.ycor() > 280 or Control.head.xcor() < -280 or Control.head.ycor() < -280:
        play = False
        Board.detect_wall()
    
    for body in Snake.body[1:]: # Slicing
        if Control.head.distance(body) < 10:
            play = False
            Board.detect_wall()

screen.exitonclick()