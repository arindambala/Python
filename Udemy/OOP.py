# Day 16 - 100 Days of Code

# Procedural Programming || Object Oriented Programming (OOP)
print(f"\n---- Object Oriented Programming ----\n")

# Classes & Objects
# Class - Blueprint / Template to create objects || Object - Instance of a class

# class Deck:
    # def __init__(self, dealer = False):
    # self.card = card
    # self.dealer = dealer
    
    # def add_card(self, card_list):
    # self.cards.extend(card_list)
    
    # def calc_value(self):
    # self.value = 0
    # has_ace = False
    
    # for card in self.cards:
        # card_value = int(card.rank['Value'])
        # self.value += card_value
        # if card.rank['Rank'] == 'A':
            # has_ace = True
    
    # if has_ace and self.value > 21:
        # self.value -= 10
    
    # def get_value(self):
        # self.calc_value()
        # return self.value
    
    # def blackJack(self):
        # return self.get_value() == 21

    # def display(self, show_dealer_cards = False):
        # print(f'''\n__ {"Dealer's" if self.dealer else "Player's"} Hand : __\n''')
        # for index, card in enumerate(self.cards):
            # if index == 0 and self.dealer and not show_dealer_cards and not self.blackJack():
                # print("Hidden!")
            # else:
                # print(card)
        
        # if not self.dealer:
            # print("\nValue : ", self.get_value())
        # print()

# class Game:
    # def play(self):
        # game_number = 0
        # games_to_play = 0
        
        # while games_to_play <= 0:
            # try:
                # games_to_play = int(input("\nHow mant times? : "))
            # except:
                # print("\nINVAID!")
        
        # while game_number < games_to_play:
            # game_number += 1
            
            # deck = Deck()
            # deck.card_shuffler()
            
            # player = Hand()
            # dealer = Hand(dealer = True)
            
            # for _ in range(2):
                # player.add_card(deck.card_deal(1))
                # dealer.add_card(deck.card_deal(1))