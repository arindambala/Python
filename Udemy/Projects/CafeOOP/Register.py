class CashRegister:
    
    CURRENCY = '$'
    
    COIN_VALUES = {
        "qaurters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """ Prints the current profit """
        print(f"Money : {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """ Returns the total calculated from inserted coins """
        print("\n Print insert coins....! \n")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}? : ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """ Returns True when payment is accepted, else False """
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change. ")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("\n|> Sorry! That's not enough money. Refunded! \n")
            self.money_received = 0
            return False