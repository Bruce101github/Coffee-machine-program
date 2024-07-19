class Resource:
    """Manages and store resources for coffee machine."""

    def __init__(self):
        """Initializes resources for the coffee machine"""
        self.water = 0
        self.milk = 0
        self.coffee = 0
        self.money = 0

    def report_resources(self):
        """This prints out the remaining amount of all resources"""
        print(f"Water : {str(self.water)}ml")
        print(f"Milk : {str(self.milk)}ml")
        print(f"Coffee : {str(self.coffee)}g")
        print(f"Money : {str(self.money)}$")

    def update_resources(self, item, amount):
        """This refills the resources"""
        if item.lower() == "water":
            self.water += amount
        if item.lower() == "milk":
            self.milk += amount
        if item.lower() == "coffee":
            self.coffee += amount

    def check_resources(self, coffe_type, quantity=1):
        """Checks if there is sufficient resources make coffee"""
        message = []
        if coffe_type.lower() == "espresso":
            if (self.water > 30 * quantity and 
                    self.coffee > 9 * quantity):
                return True
            else:
                if self.water < (30 * quantity):
                    message.append("Sorry there is not enough water.")
                if self.coffee < (9 * quantity):
                    message.append("Sorry there is not enough coffee.")
                return "\n".join(message)
        if coffe_type.lower() == "latte" or "cappuccino":
            if (self.water > (60 * quantity) and 
                    self.coffee > (18 * quantity) and 
                    self.milk > (60 * quantity)):
                return True
            else:
                if self.water < (60 * quantity):
                    message.append("Sorry there is not enough water.")
                if self.coffee < (18 * quantity):
                    message.append("Sorry there is not enough coffee.")
                if self.milk < (60 * quantity):
                    message.append("Sorry there is not enough milk.")
                return "\n".join(message)



