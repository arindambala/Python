# Day 25 - 100 Days of Code

import turtle

screen = turtle.Screen()
screen.title('U.S. States Guess')

img = 'blank_states_img.gif'
screen.addshape(img)

turtle.shape(img)

guess = screen.textinput(title='Guess the State!', prompt='Which state to be found?')
print(guess)

screen.exitonclick()