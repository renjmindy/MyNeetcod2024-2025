from sortedcontainers import SortedDict

# TODO: Define a Product class with attributes id (integer) and name (string). 
# Ensure this class supports comparison based on the id only for sorting.
class Product:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def __lt__(self, other):
        return (self.id) < (other.id)

    def __gt__(self, other):
        return (self.id) > (other.id)

    def __eq__(self, other):
        return (self.id) == (other.id)

    def __ne__(self, other):
        return (self.id) != (other.id)    
        
    def __hash__(self):
        return hash((self.id, self.name))
        
# TODO: Create an instance of SortedDict named inventory.
inventory = SortedDict()

# TODO: Add some Product objects to inventory with different ids and names, associating each Product with an integer stock quantity.
inventory[Product(101, 'Prok')] = 5
inventory[Product(102, 'Chicken')] = 15
inventory[Product(103, 'Beef')] = 10
inventory[Product(104, 'Spinach')] = 10

# TODO: Use the bisect_left method to find the index of the first Product object with an id not less than a specified value.
print(inventory.bisect_left(Product(101, 'Pork')))

# TODO: Use the peekitem method to display the Product and its stock quantity at the found index.
print(inventory.peekitem(inventory.bisect_left(Product(101, 'Prok')))[1])
