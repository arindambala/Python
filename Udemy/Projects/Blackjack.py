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

def victory_check(player_calc, dealer_calc):
    if player_calc == dealer_calc:
        return "\n|>Draw!"
    elif dealer_calc == 0:
        return "\n|> Lost! Pack it up cause Dealer has Blackjack!"
    elif player_calc == 0:
        return "\n|> Won! Player takes it home with Blackjack!"
    elif dealer_calc > 21:
        return "\n|> Won! Dealer went over the roof!"
    elif player_calc > 21:
        return "\n|> Lost! Player broke the ceiling!"
    elif player_calc > dealer_calc:
        return "\n|> Won! Player did something for themselves!"
    else:
        return "\n|> Loss! Dealer ain't a bust case!"

def play_game():
    # print(BLACKJACK_LOGO)
    player_cards, dealer_cards = [], []
    player_score, dealer_score = -1, -1
    game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not game_over:
        # Player
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

    while dealer_score != 0 and dealer_score < 17:
        # Dealer
        dealer_cards.append(deal_card())
        dealer_score = calc_score(dealer_cards)

    print(f"\nPlayer _FINAL_ Hand : {player_cards}, Player _FINAL_ Score : {player_score}")
    print(f"Dealer _FINAL_ Hand : {dealer_cards}, Dealer _FINAL_ Score : {dealer_score}")
    print(victory_check(player_score, dealer_score))

while input("\nDo you want to play Blackjack? (Y | N) : ").lower() == 'y':
    # print("\n" * 30)
    play_game()