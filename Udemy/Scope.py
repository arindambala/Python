# Day 13 - 100 Days of Code

from random import randint

# Constants
EASY_LVL_TURNS = 5
HARD_LVL_TURNS = 3

# GUESSNUMLOGO = '''
#     ____ __   __ ___  ___ ___
#     / _` | | | |/ _ \/ __/ __|
#     | (_| | |_| |  __/\__ \__ \
#     \__, |\__,_|\___||___/___/
#     __/ |                    
#     |___/     '''

# Guess the number
print(f"\n---- Welcome to Guess the Number! ----")

def check_guess(player_guess, actual_guess, turns):
    ''' Checks num against guess & returns remaining number of turns '''
    if player_guess > actual_guess:
        print("_ HIGH. Please RETRY with a LOWER number! _")
        return turns - 1
    elif player_guess < actual_guess:
        print("_ LOW. Please RETRY with a HIGHER number! _")
        return turns - 1
    else:
        print(f"\n|> LET'S GO! The GUESS was {actual_guess} ! CONGRATULATIONS! \n")

def set_diff():
    lvl = input("\nDifficulty of the game? (Easy | Hard) : ").lower()
    if lvl == 'easy':
        return EASY_LVL_TURNS
    else:
        return HARD_LVL_TURNS

def game():
    # print(GUESSNUMLOGO)
    print(f"\n---- What number between 1 & 100 has been thought of? ----\n")
    num = randint(1, 100)
    # print(f"The guessed number : {num}")

    turns = set_diff()

    guess = 0
    while guess != num:
        print(f"\nAttempts remaining : {turns}")

        guess = int(input("\nPlayer guessed : "))

        turns = check_guess(guess, num, turns)

        if turns == 0:
            print(f"\n|> LOST! The GUESS was {num} ! OUT OF GUESSES! \n")
            return

game()