class CoffeeMachine:
    def __init__(self):
        self.__coffee_level = 0  # Public attribute

    def make_coffee(self):
        if self.__coffee_level > 0:
            print("Enjoy your coffee!")
            self.__coffee_level -= 1
        else:
            print("Please refill coffee!")

    # TODO: Add missing method to refill coffee
    def refill_coffee(self, amount):
        self.__coffee_level += amount
        
    # The method takes the amount to refill and adds it to the current coffee amount

machine = CoffeeMachine()
machine.refill_coffee(3)  # Refilling the machine using the method
machine.make_coffee()  # Produces one cup of coffee
machine.make_coffee()  # Produces another cup of coffee
