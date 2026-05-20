# Day 19 - 100 Days of Code

from turtle import Turtle, Screen
import random

print(f"\n---- Turt ^ Race ----\n")

screen = Screen()
screen.setup(width=500, height=400)

bet = screen.textinput(title='Ight Bet', prompt="Which turtle has thy bet? (Colour) : ")
# print(bet)
colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
y_pos = [-100, -70, -40, -10, 20, 50, 80]
turts = []

for turt_index in range(0, 7): # Instances
    turt = Turtle(shape='turtle')
    turt.penup()
    turt.color(colors[turt_index])
    turt.goto(x=-230, y=y_pos[turt_index])
    turts.append(turt)

race = False
if bet:
    race = True

while race:
    for turtles in turts: # States
        if turtles.xcor() > 230:
            race = False
            won_turt = turtles.pencolor()
            if won_turt == bet:
                print(f"|> Bet WON! The {won_turt} turtle has won the turtle race! \n")
            else:
                print(f"|> Bet LOST! The {won_turt} turtle has won the turtle race! \n")
        
        random_dist = random.randint(0, 10)
        turtles.forward(random_dist)

screen.exitonclick()