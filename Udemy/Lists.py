# Day 4 - 100 Days of Code

import random

# Rock
rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
'''

# Paper
paper = '''
        _______
    ---'    ____)____
                ______)
                _______)
                _______)
    ---.__________)
'''

# Scissors
scissors = '''
        _______
    ---'   ____)____
                ______)
            __________)
        (____)
    ---.__(___)
'''

HAND = [rock, paper, scissors]

# Rock Paper Scissors Game
print(f"\n---- Welcome to Rock Paper Scissors Game! ----")

user_choice = int(input("\nWhat's the choice? (0 | Rock, 1 | Paper or 2 | Scissors) : "))
print("\nUser chose : \n")
if user_choice >= 0 and user_choice <= 2:
    print(HAND[user_choice])

comp_choice = random.randint(0, 2)
print("\nComputer chose : \n")
print(HAND[comp_choice])

# print(f"\nUser : {user_choice} | Computer : {comp_choice}")

if user_choice >= 3 or user_choice < 0:
    print("\n\n____ INVALID! User Loses! ____") 
elif user_choice == 0 and comp_choice == 2:
    print("\n\n____ User Wins! ____")
elif comp_choice == 0 and user_choice == 2:
    print("\n\n____ Computer Wins! ____")
elif comp_choice > user_choice:
    print("\n\n____ Computer Wins! ____")
elif user_choice > comp_choice:
    print("\n\n____ User Wins! ____")
elif comp_choice == user_choice:
    print("\n\n____ That's a Draw! ____")