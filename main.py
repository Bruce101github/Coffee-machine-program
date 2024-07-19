from resources import Resource
from coin_processing import Coin
from coffee import Coffee

class Main(Coin, Coffee):
    """This controls the main program"""

    def __init__(self):
        """Initialization"""
        Coin.__init__(self)
        Coffee.__init__(self)
        self.prompt = input("what would you like?(espresso/latte/cuppuccino): ").lower()
    
    def proccess_order(self):
        sufficient = super().check_resources(self.prompt)
        if sufficient is True:
            change = super().proccess_coins(self.prompt)
            if change >= 0:
                super().make_coffee(self.prompt)
                if change > 0:
                    print(f"Here is ${str(format(change, ".2f"))} dollars in change.")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(sufficient)
           

active = True

while active == True:
    coffee = Main()
    coffee.update_resources("water", 500)
    coffee.update_resources("milk", 500)
    coffee.update_resources("coffee", 500)

    coffee.proccess_order()


