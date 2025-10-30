class Laptop:
    def __init__(self, model, price):
        self.__model = model    # Private attribute for the laptop's model
        self.__price = price    # Private attribute for the laptop's price

    # TODO: Restore the method to retrieve the laptop model
    def get_model(self):
        return self.__model
    # TODO: Implement a setter method for price that validates price is not negative
    def set_price(self, amount):
        if amount < 0: return "Error: Price must be positive"
        else: self.__price = amount

# Example usage:
my_laptop = Laptop('ThinkPad X1', 1500)
# Assume the method to update the price is correctly implemented
my_laptop.set_price(1200)       # Update the price
# Assume the method to retrieve the model is correctly implemented and use it here
print(my_laptop.get_model())    # Expected to print 'ThinkPad X1'
print(my_laptop.set_price(-100)) # Expected to print: "Error: Price must be positive"
