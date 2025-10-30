class Toaster:
    def __init__(self):
        self.__bread_slots = 2  # Private attribute for bread slots

    def get_bread_slots(self):  # Getter method for bread slots
        return self.__bread_slots
        
    def set_bread_slots(self, amount):  # Setter method for bread slots
        self.__bread_slots += amount
        return self.__bread_slots

# Example without encapsulation
toaster = Toaster()
toaster.set_bread_slots(6)  # Attempt to set the new number of slots
print(toaster.get_bread_slots()) # Expected to print: 4
