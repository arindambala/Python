# Day 12 - 100 Days of Code

# Capstone Project : Blackjack
print(f"\n---- Welcome to Blackjack! ----\n")

# print("\n Hand : Card")
print("\n Card - Rank : ")

# Use a dictionary - Card Values w.r.t Ranks
dict = {'A': 10, 'K' : 10, 'Q' : 10, 'J' : 10} # Face cards // Other cards | Same as the number - {1, 2, 3,...}

# With 'class' | Without 'class' - Already committed on other program

play = 0 # Rank - Value ? Player : Dealer
play_count = 0, dealer_play = 0, dealer_hold = 0 # Count number of times play took place also | Print if required

# card & deck classes
card_dealer, card_shuffler = 0, 0
# deck class to be added | shuffler class to be added

suit = 0 # Add random module
# Random selection gives the illusion of a real blackjack game

deck_choice = [1, 2, 3, 4]
suit = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
# Number of players might not be more than just the player & the dealer

Card, Deck, Hand, Game = [] # Classes to be considered
# Set suit class - init main for Game class? - Yes | Win & Play functions to be implemented

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return (f"{self.rank['Rank']} of {self.suit}")

class Deck:
    def __init__(self):
        self.cards = []

# Flowchart - Contextual | Simple or Detailed? | Control Flow
play_count = 0 # Increment by prompt | Ask for replay | Output last state

# Functions to be used - card_deal(), card_shuffle(), play() | User Choice

class victory_check:
    while True:
        print("Winner? ")
        # if | elif | else

        # if not game_over(): | else:
    # start = Game() | start.play()

    # if player_val > dealer_val : WIN | elif dealer_val > player_val : LOSS | else DRAW

# continued : Check the code with - 'class'
# commit - Twenty One | FreeCodeCamp - YouTube