# Day 25 - 100 Days of Code

import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Guess')

img = 'blank_states_img.gif'
screen.addshape(img)

turtle.shape(img)

data = pandas.read_csv('50_states.csv')
states = data.state.to_list()
states_guessed = []

while len(states_guessed) < 50:
    guess = screen.textinput(title=f'{len(states_guessed)}/50 States', prompt='Which state to be found?').title()
    # print(guess)

    if guess == 'Exit':
        states_missed = []
        for state in states:
            if state not in states_guessed:
                states_missed.append(state)
        # print(states_missed)
        learn = pandas.DataFrame(states_missed)
        learn.to_csv('learn_states.csv')
        break
    
    if guess in states:
        states_guessed.append(guess)
        bloom = turtle.Turtle()
        bloom.hideturtle()
        bloom.penup()
        
        state_data = data[data.state == guess]
        bloom.goto(state_data.x.item(), state_data.y.item())
        # bloom.write(state_data.state.item())
        bloom.write(guess)