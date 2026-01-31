'''

# Program to demonstarte a game of Blackjack - FreeCodeCamp | YouTube.
# This code is released on a personal computer.
# (c) 2026, Arindam Bala.

'''

import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return (f"{self.rank['Rank']} of {self.suit}")

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
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
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def card_shuffler(self):
        if (len(self.cards) > 1):
            random.shuffle(self.cards)

    def card_deal(self, number):
        cards_dealt = []
        for _ in range(number):
            if (len(self.cards) > 0):
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt

        # card_shuffler()
        # card = card_deal(1)[0]

        # print(card[1]['Value'])
        # cards_dealt = card_deal(2)
        # card = cards_dealt[0]
        # rank = card[1]

        # if (rank == 'A'):
        #     value = 11
        # elif (rank == 'J' or rank == 'Q' or rank == 'K'):
        #     value = 10
        # else:
        #     value = rank

        # rank_dict = {'Rank': rank, 'Value': value}
        # print(rank_dict['Rank'], rank_dict['Value'])

# card1 = Card('Hearts', {'Rank': 'J', 'Value': 10})
# print(card1)

# deck1 = Deck()
# deck2 = Deck()
# deck2.card_shuffler()
# print(deck1.cards)
# print(deck2.cards)

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
    
    def get_value(self):
        self.calc_value()
        return self.value
    
    def blackJack(self):
        return self.get_value() == 21
    
    def display(self, show_dealer_cards = False):
        print(f'''\n____ {"Dealer's" if self.dealer else "Player's"} Hand :  ____\n''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_dealer_cards and not self.blackJack():
                print("Hidden!")
            else:
                print(card)
        
        if not self.dealer:
            print("\nValue : ", self.get_value())
        print()

# deck = Deck()
# deck.card_shuffler()

# hand = Hand()
# hand.add_card(deck.card_deal(2))
# hand.display()

class Game:
    def play(self):
        game_number = 0
        games_to_play = 0
        
        while games_to_play <= 0:
            try:
                games_to_play = int(input("\nHow many times does the play happen? : "))
            except:
                print("\n____ INVALID! Correct input required! ____")
        
        while game_number < games_to_play:
            game_number += 1
            
            deck = Deck()
            deck.card_shuffler()
            
            player = Hand()
            dealer = Hand(dealer = True)
            
            for _ in range(2):
                player.add_card(deck.card_deal(1))
                dealer.add_card(deck.card_deal(1))
            
            print()
            print('*' * 30)
            print(f"____ Game {game_number} of {games_to_play} ! ____")
            print('*' * 30)
            player.display()
            dealer.display()
            
            if self.victory_check(player, dealer):
                continue
            
            choice = ''
            while player.get_value() < 21 and choice not in ['s', 'stand']:
                choice = input("\nChoice? (Hit | Stand) : ").lower()
                print()
                while choice not in ['h', 's', 'hit', 'stand']:
                    choice = input("\nChoice must be either 'Hit' or 'Stand' (H | S) : ").lower()
                    print()
                if choice in ['h', 'hit']:
                    player.add_card(deck.card_deal(1))
                    player.display()
        
            if self.victory_check(player, dealer):
                continue
            
            player_hand = player.get_value()
            dealer_hand = dealer.get_value()
            
            while dealer_hand < 17:
                dealer.add_card(deck.card_deal(1))
                dealer_hand = dealer.get_value()
            
            dealer.display(show_dealer_cards = True)
            
            if self.victory_check(player, dealer):
                continue
            
            print("\n\n____ FINAL RESULTS ____\n")
            print(f"Player Hand : {player_hand} | Dealer Hand : {dealer_hand}")
            
            self.victory_check(player, dealer, True)
        
        print("\n\n____ THANK YOU! HOPE YOU HAD FUN! ____")

    def victory_check(self, player, dealer, game_over = False):
        if not game_over:
            if player.get_value() > 21:
                print("\n\n____ You're BUSTED! Dealer Wins! NEXT TIME MATE! ____")
                return True
            elif dealer.get_value() > 21:
                print("\n\n____ Dealer BUSTED! You Win! CONGRATULATIONS! ____")
                return True
            elif player.blackJack() and dealer.blackJack():
                print("\n\n____ DRAW! ____")
                return True
            elif player.blackJack():
                print("\n\n____ You've BlackJack! You Win! CONGRATULATIONS! ____")
                return True
            elif dealer.blackJack():
                print("\n\n____ Dealer has BlackJack! Dealer Wins! NEXT TIME MATE! ____")
                return True
        
        else:
            if player.get_value() > dealer.get_value():
                print("\n\n___ You win! CONGRATULATIONS! ____")
            elif player.get_value() == dealer.get_value():
                print("\n\n___ DRAW! ____")
            else:
                print("\n\n____ Dealer Wins! NEXT TIME MATE! ____")
            return True
        return False

start = Game()
start.play()