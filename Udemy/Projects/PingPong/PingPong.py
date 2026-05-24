# Day 22 - 100 Days of Code

from turtle import Screen
from Paddle import Paddle
from Ball import Ball
import time

print(f"\n---- Ping ^ Pong ----\n")

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Ping | Pong')
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkey(left_paddle.move_paddle_up, 'w')
screen.onkey(left_paddle.move_paddle_down, 's')
screen.onkey(right_paddle.move_paddle_up, 'Up')
screen.onkey(right_paddle.move_paddle_down, 'Down')

play = True
while play:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ball()

screen.exitonclick()