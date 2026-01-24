# Day 3 - 100 Days of Code

# Treasure Hunt
print('''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/[TomekK]
    *******************************************************************************
''') # ascii.co.uk | Website

print(f"\n---- Welcome to Treasure Island! ----")
print(f"\n---- Not every path will lead to the Treasure! ----\n")

choice_road = input("\nThe crossroad defines the fate. What's the choice? (Left | Right) : ").strip().lower()
if choice_road == 'left':
    
    choice_lake = input("\nThe lake sees beyond the naked eye. The island might be a safe haven, but time waits for no one. Will the boat be a rescue or fate could be carved through one's own hands? What's the choice? (Wait | Swim) : ").strip().lower()
    
    if choice_lake == 'wait':
        choice_door = input("\nThe unharmed arrival at the island blesses with a house. The doors of the house conclude the path, but it's not all sunshine & rainbows with the colours! What's the choice? (Red | Yellow | Blue) : ").strip().lower()
        
        if choice_door == 'yellow':
            print("\n\n____ The treasure belongs to those who dare to make a choice. CONGRATULATIONS! ____")
        elif choice_door == 'red':
            print("\n\n____ GAME OVER - The fire within can never suffice to the fire that surrounds one! ____")
        elif choice_door == 'blue':
            print("\n\n____ GAME OVER - To be devoured by a beast is also fate! ____")
        else:
            print("\n\n____ GAME OVER - The choices don't matter if they don't exist in the first place! ____")

    else:
        print("\n\n____ GAME OVER - A feast has arrived for the crocodiles of the lake! ____")

else:
    print("\n\n____ GAME OVER - The void got a treat! ____")