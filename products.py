class Product:
    def __init__(self, name, price, quantity):
        # Initialize instance variables
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

        # Validate input values
        if self.name == "":
            raise ValueError("Sorry, the product name cannot be empty.")
        if self.price < 0:
            raise ValueError("Sorry, the price cannot be below zero.")
        if self.quantity < 0:
            raise ValueError("Sorry, the quantity cannot be below zero.")

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity <= 0:
            self.quantity = 0
            self.deactivate()

    def is_active(self):
        return self.active and self.quantity > 0  # Update the condition

    def activate(self):
        if not self.is_active():
            self.active = True

    def deactivate(self):
        if self.is_active():
            self.active = False
        else:
            raise Exception("Product deactivation is not allowed.")

    def show(self):
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if not self.is_active():
            raise Exception("The product is currently deactivated.")

        if quantity <= 0:
            raise Exception("Please provide a positive quantity to purchase.")

        if quantity > self.quantity:
            raise Exception("Insufficient quantity available for purchase.")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)

        if self.quantity == 0:
            self.deactivate()

        return total_price
