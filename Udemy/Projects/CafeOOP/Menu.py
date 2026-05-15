class MenuItem:
    """ Models each menu item """
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class MenuChoice:
    """ Models the menu with drinks """
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappucino", water=250, milk=50, coffee=24, cost=3)
        ]

    def get_items(self):
        """ Returns all the names of the available menu """
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """ Searches the menu for a particular drink by name and returns that item if it exists, otherwise return none """
        for item in self.menu:
            if item.name == order_name:
                return item
        print("\n|> Sorry! That item isn't available \n")