# Day 15 - 100 Days of Code

from Menu import MENU, RESOURCES

print(f"\n---- Caffeine ^ Infinity ----\n")

def sufficient_resources(ingredients_order):
    """ Returns the possibility of the acceptance of the order """
    for item in ingredients_order:
        if ingredients_order[item] >= RESOURCES[item]:
            print(f"\n|> SORRY! Ain't enough {item} left. \n")
            return False
    return True

def money_system():
    """ Returns the total calculated amount of inserted coins """
    print("\nPlease insert the required coins : ")
    total = int(input("Quarters : ")) * 0.25
    total += int(input("Dimes : ")) * 0.1
    total += int(input("Nickels : ")) * 0.05
    total += int(input("Pennies : ")) * 0.01
    return total

def successful_transaction(received_payment, drink_cost):
    """ Returns the status of the payment done """
    if received_payment >= drink_cost:
        change = round(received_payment - drink_cost, 2)
        print(f"\n|> Change : {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("\n|> SORRY! Ain't enough bread. Money refunded. \n")
        return False

def coffee_maker(drink_name, ingredients_order):
    """ Deduct the required ingredients from the available resources """
    for item in ingredients_order:
        RESOURCES[item] -= ingredients_order[item]
    print(f"\n|> Thy ORDER : {drink_name}☕ \n")

is_on = True
profit = 0

while is_on:
    choice = input("What's on thy mind today? (Espresso | Latte | Cappuccino) : ").lower()

    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"\nWater : {RESOURCES['water']} ml")
        print(f"Milk : {RESOURCES['milk']} ml")
        print(f"Coffee : {RESOURCES['coffee']} g")
        print(f"Money : $ {profit} \n")
    else:
        drink = MENU[choice]
        if sufficient_resources(drink['ingredients']): # print(f"\n{drink}")
            payment = money_system()
            if successful_transaction(payment, drink['cost']):
                coffee_maker(choice, drink['ingredients'])