# Day 12 - 100 Days of Code

import random

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
        suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
        ranks = [
                {'Rank': 'A', 'Value': 11},  
                {'Rank': '2', 'Value': 2},
                {'Rank': '3', 'Value': 3},
                {'Rank': '4', 'Value': 4},
                {'Rank': '5', 'Value': 5},
                {'Rank': '6', 'Value': 6},
                {'Rank': '7', 'Value': 7},
                {'Rank': '8', 'Value': 8},
                {'Rank': '9', 'Value': 9},
                {'Rank': '10', 'Value':10},
                {'Rank': 'J', 'Value': 10},
                {'Rank': 'Q', 'Value': 10},
                {'Rank': 'K', 'Value': 10},
            ]
        
        for suit in suits:
            self.cards.append(Card(suit))
    
    def card_shuffler(self):
        if (len(self.cards) > 1):
            random.shuffle(self.cards)
    
    def card_deal(self, number):
        cards_dealt = []
        for _ in range(number):
            if (len(self.cards) > 0):
                card = self.card.pop()
                cards_dealt.append(card)
        return cards_dealt

class Hand:
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer
    
    def add_card(self, card_list):
        self.cards.extend(card_list)
    
    def calc_value(self):
        self.value = 0
        has_ace = False
        
        for card in self.cards:
            card_value = int(card.rank['Value'])
            self.value += card_value
            if card.rank['Rank'] == 'A':
                has_ace = True
        
        if has_ace and self.value > 21:
            self.value -= 10

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