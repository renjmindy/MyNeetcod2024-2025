class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        return f"Product: {self.name}, Price: ${self.price:.2f}"

# TODO: Implement the PromotionalProduct subclass that inherits from Product.
# This subclass should introduce a promotional message and discount percentage.
# It should override the display method to include the promotion and the discounted price.
# The add_promotion method should accept a message and discount, storing these for later use.
class PromotionalProduct(Product):
    def add_promotion(self, message, discount):
        self.message = message
        self.discount = discount
    def display(self):
        return f"Product: {self.name}, Original Price: ${self.price:.2f}, Promotion: {self.message}, Final Price: ${self.price - (self.price * self.discount * 0.01):.2f}"
