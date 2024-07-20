from resources import Resource
from coin_processing import Coin
from coffee import Coffee

active = True

class Main(Coin, Coffee):
    """This controls the main program"""

    def __init__(self):
        """Initialization"""
        Coin.__init__(self)
        Coffee.__init__(self)
        self.prompt = input("what would you like?(espresso/latte/cuppuccino): ").lower()
    
    def proccess_order(self):
        if (self.prompt == "espresso" or 
            self.prompt == "latte" or 
            self.prompt == "cappuccino"):
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
        elif self.prompt == "report":
            super().report_resources()
        elif self.prompt == "off":
            active = False
        else:
            print("Unknown command. Try again!")



while active == True:
    coffee = Main()
    coffee.update_resources("water", 500)
    coffee.update_resources("milk", 500)
    coffee.update_resources("coffee", 500)
    coffee.proccess_order()
    if coffee.prompt == "off":
        break

