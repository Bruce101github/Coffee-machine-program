from resources import Resource
from coin_processing import Coin


class Coffee(Resource):
    """Handles the making of the coffee"""

    def __init__(self):
        """Initialize"""
        super().__init__()

    def make_coffee(self, coffee, quantity=1):
        """Makes coffee if there is sufficient resources and paid"""
        if coffee.lower() == "espresso":
            self.water -= (30 * quantity)
            self.coffee -= (9 * quantity)
            self.money += (1 * quantity) 
            print(f"Here is your {coffee.lower()}. Enjoy!")

        elif coffee.lower() == "latte" or "cappuccino":
            self.water -= (60 * quantity)
            self.coffee -= (18 * quantity)
            self.milk -= (60 * quantity)
            self.money += (3 * quantity)
            print(f"Here is your {coffee.lower()}. Enjoy!")



