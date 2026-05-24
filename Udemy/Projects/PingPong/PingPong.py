# Day 22 - 100 Days of Code

from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from Score import ScoreBoard
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
board = ScoreBoard()

screen.listen()
screen.onkey(left_paddle.move_paddle_up, 'w')
screen.onkey(left_paddle.move_paddle_down, 's')
screen.onkey(right_paddle.move_paddle_up, 'Up')
screen.onkey(right_paddle.move_paddle_down, 'Down')

play = True
while play:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()
    
    if ball.ycor() > 280 or ball.ycor() < -280: # Wall
        ball.bounce_ball_y()
    
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320 or ball.distance(right_paddle) < 50 and ball.xcor() > 320: # Paddle
        if ball.x_move > 0 or ball.x_move < 0: # Multi bounce
            ball.bounce_ball_x()
    
    if ball.xcor() > 380:
        ball.reset_ball()
        board.left_player_point()
    
    if ball.xcor() < -380:
        ball.reset_ball()
        board.right_player_point()

screen.exitonclick()