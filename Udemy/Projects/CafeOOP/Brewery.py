class Brewery:
    """ Models the machine that makes the coffee """
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """ Prints a report of all resources """
        print(f"Water : {self.resources['water']} ml")
        print(f"Milk: {self.resources['milk']} ml")
        print(f"Coffee : {self.resources['coffee']} ml")

    def sufficient_resources(self, drink):
        """ Returns the possibility of acceptance of the order """
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"\n|> SORRY! Ain't enough {item} left. \n")
                can_make = False
        return can_make

    def coffee_maker(self, order):
        """ Deduct the required ingredients from the available resources """
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"\n|> Thy ORDER : {order.name}☕ \n")