class Coin:
    """Mange and process all payment"""

    def __init__(self):
        """Initialize the prices of coffee"""
        self.price_espresso = 1
        self.price_latte = 3
        self.price_cappuccino = 3

    def proccess_coins(self, coffee, quantity=1):
        """Check and take payment for order"""
        if coffee == "espresso":
            price = self.price_espresso * quantity
        if coffee == "latte":
            price = self.price_latte * quantity
        if coffee == "cappuccino":
            price = self.price_cappuccino * quantity

        print(f"Your order for {str(quantity)} {coffee} is ${str(price)}")

        print(f"\nInsert coins according to denominations.\nEnter 0 if you money doesn't include listed denomination.")

        dollars = int(input("Insert dollars:\n"))
        quaters = int(input("Insert quaters:\n")) * 0.25
        dimes = int(input("Insert dimes:\n")) * 0.10
        nickles = int(input("Insert nickles:\n")) * 0.05
        pennies = int(input("Insert pennies:\n")) * 0.01

        total_coins = dollars + quaters + dimes + nickles + pennies
        change = total_coins - price

        return change


