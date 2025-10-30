from sortedcontainers import SortedDict

# TODO: Define the OrderManager class
# This class should manage orders using a SortedDict where priorities determine the order processing sequence
class OrderManager:
    def __init__(self):
        self.order = SortedDict()
        
    def add_order(self, customer, priority):
# TODO: Add the `add_order(customer, priority)` method to the class - it should map the customer to its priority (priority is stored as a key)
        self.order[priority] = customer

# TODO: Add the `process_order()` method that processes the order with the highest priority (the order is removed after processing)
    def process_order(self):
        if self.order: return self.order.popitem(0)
        else: "No more orders to proceed"

# TODO: Initialize the OrderManager class
orders = OrderManager()
# TODO: Add a couple of orders using the add_order method, with a unique priority for each
orders.add_order("Mary", 2)
orders.add_order("John", 1)
orders.add_order("Paddy", 4)
orders.add_order("Pearson", 5)
# TODO: Retrieve and print the next order to process - the one with the highest priority
print(orders.process_order())
