# Day 22 - 100 Days of Code

from turtle import Turtle, Screen

print(f"\n---- Ping ^ Pong ----\n")

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Ping | Pong')
screen.tracer(0)

paddle = Turtle()
paddle.shape('square')
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.color('white')
paddle.penup()
paddle.goto(350, 0)

def move_paddle_up():
    pos_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), pos_y)

def move_paddle_down():
    pos_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), pos_y)

screen.listen()
screen.onkey(move_paddle_up, 'Up')
screen.onkey(move_paddle_down, 'Down')

play = True
while play:
    screen.update()

screen.exitonclick()