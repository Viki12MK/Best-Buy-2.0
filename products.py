
class Product:
    def __init__(self, name, price, quantity):
        # Initialize instance variables
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

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

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def show(self):
        promotion_name = self.promotion.__class__.__name__ if self.promotion else "None"
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion: {promotion_name}"
        # return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

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


class NonStockedProduct(Product):
    def __init__(self, name, price, quantity=0):
        super().__init__(name, price, quantity)

    def show(self):
        return f"Product: {self.name}, Price: {self.price}, Non-Stocked"


class LimitedProduct(Product):
    def __init__(self, name, price, maximum, quantity=0):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}"
