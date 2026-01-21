'''

# Program to demonstarte a game of rock, paper & scissors - FreeCodeCamp | YouTube.
# This code is released on a personal computer.
# (c) 2026, Arindam Bala.

'''

import random

# Move map to what defeats
RULES = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

VALID_CHOICES = tuple(RULES.keys())

def get_player_choice():
    while True:
        choice = input("\nEnter player choice (rock, paper or scissors) : ").strip().lower()
        if choice in VALID_CHOICES:
            return choice
        print("\nINVALID! Please try again.")

def get_computer_choice():
    return random.choice(VALID_CHOICES)

def ask_to_replay():
    while True:
        reply = input("\nWould you like to play again? (y/n) : ").strip().lower()
        if reply in ('y', 'n'):
            return reply == 'y'
        print("\nINVALID! Please enter 'y' or 'n'. ")

def victory_check(player, computer):
    if (player == computer):
        return "Draw"
    elif (RULES[player] == computer):
        return "Player"
    else:
        return "Computer"

def play_game():
    player_score = 0
    computer_score = 0
    round_number = 1
    
    print("\nWELCOME to RPS - Rock, Paper & Scissors!")
    
    while True:
        print(f"\n---- ROUND {round_number} ----")
        
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nPlayer choice : {player_choice}")
        print(f"Computer choice: {computer_choice}")
        
        result = victory_check(player_choice, computer_choice)
        
        if (result == "Player"):
            player_score += 1
            print("\n |> YOU WIN the round!")
        elif (result == "Computer"):
            computer_score += 1
            print("\n |> COMPUTER WINS the round!")
        else:
            print("\n |> It's A DRAW!")

        print(f"\n |> SCORE -> Player : {player_score} | Computer : {computer_score}")

        if not ask_to_replay():
            break

        round_number += 1

    print("\n---- FINAL SCORE ----")
    print(f"\n |> Player : {player_score} | Computer: {computer_score}")
    
    if (player_score > computer_score):
        print("\n____ Overall Result :: WINNER |> PLAYER! ____")
    elif (computer_score > player_score):
        print("\n____ Overall Result :: WINNER |> COMPUTER! ____")
    else:
        print("\n____ Overall Result :: DRAW! ____")

    print("\n_---- Good game, Well played! Appreciate it. ----_")

if __name__ == "__main__":
    play_game()

# def get_turn():
#     options = ['rock', 'paper', 'scissors']
#     play_turn = input("\nEnter a option (rock, paper, scissors) : ")
#     comp_turn = random.choice(options)

#     turns = {
#         'Player': play_turn,
#         'Computer': comp_turn
#     }
    
#     return turns

# # def greet():
# #     return "Hi"

# # response = greet()
# # print(response) # Hi

# def win_check(player, computer):
#     print(f"Player choice was {player} & Computer choice was {computer}, hence : \n")
    
#     if (player == computer):
#         return "Draw!"
#     elif (player == 'rock'): 
#         if (computer == 'scissors'):
#             return "Rock smashed Scissors! Player WON!"
#         else:
#             return "Paper covers Rock! Computer WON!"
#     elif (player == 'paper'): 
#         if (computer == 'rock'):
#             return "Paper covers Rock! Player WON!"
#         else:
#             return "Scissors cut Paper! Computer WON!"
#     elif (player == 'scissors'): 
#         if (computer == 'paper'):
#             return "Scissors cut Paper! Player WON!"
#         else:
#             return "Rock smashed Scissors! Computer WON!"
#     else:
#         return "INVALID! Please try again!"

# turns = get_turn()
# result = win_check(turns['Player'], turns['Computer'])

# print(result)