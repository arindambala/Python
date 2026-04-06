# Day 12 - 100 Days of Code

import random

# BLACKJACK_LOGO = ''' _     _            _    _            _    
#                     | |   | |          | |  (_)          | |   
#                     | |__ | | __ _  ___| | ___  __ _  ___| | __
#                     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
#                     | |_) | | (_| | (__|   <| | (_| | (__|   < 
#                     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
#                                             _/ |                
#                                             |__/                 '''

# Capstone Project : Blackjack
print(f"\n---- Welcome to Blackjack! ----\n")

def deal_card():
    # Returns a random card from the deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calc_score(cards):
    # Takes a list of cards & returns the score calculated from the cards
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

player_cards, dealer_cards = [], []
game_over = False

for _ in range(2):
    player_cards.append(deal_card())
    dealer_cards.append(deal_card())

while not game_over:
    player_score = calc_score(player_cards)
    dealer_score = calc_score(dealer_cards)

    print(f"\nPlayer Cards : {player_cards}, Player Score : {player_score}")
    print(f"Dealer's Card : {dealer_cards[0]}")

    if player_score == 0 or dealer_score == 0 or player_score > 21:
        game_over = True
    else:
        player_deal = input("\nWould like to draw another card? (Y | N) : ").lower()
        if player_deal == 'y':
            player_cards.append(deal_card())
        else:
            game_over = True