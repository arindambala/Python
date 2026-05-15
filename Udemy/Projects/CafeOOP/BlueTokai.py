from Menu import MenuChoice, MenuItem
from Brewery import Brewery
from Register import CashRegister

print(f"\n---- Caffeine ^ Infinity ----\n")

register = CashRegister()
brewery = Brewery()
menu  = MenuChoice()

bru = True

while bru:
    options = menu.get_items()
    choice = input(f"\nWhat's on thy mind today? ({options}), or something else? : ")
    
    if choice == 'off':
        bru = False
    elif choice == 'report':
        brewery.report()
        register.report()
    else:
        drink = menu.find_drink(choice)
        # print(drink)
        if brewery.sufficient_resources(drink) and register.make_payment(drink.cost):
            brewery.coffee_maker(drink)