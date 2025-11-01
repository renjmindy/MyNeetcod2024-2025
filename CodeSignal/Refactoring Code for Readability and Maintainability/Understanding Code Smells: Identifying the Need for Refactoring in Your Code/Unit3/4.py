class InventoryItem:
    def __init__(self, name, price):
        self._name = name
        self._price = price

class ShoppingCart():
    def __init__(self):
        self.__items = dict()
    def add_items(self, item):
        self.__items[item._name] = item._price
    def calculate_total_price(self):
        return sum(self.__items.values())

# Adding items to the shopping cart

keyboard = InventoryItem("Keyboard", 99.99)
mouse = InventoryItem("mouse", 49.99)
cart = InventoryItem("cart", 149.99)
items = [keyboard, mouse, cart]

cart = ShoppingCart()

for item in items:
    cart.add_items(item)

# Calculating the total price of the cart
print(f"The total price of the shopping cart is: ${cart.calculate_total_price():.2f}")
