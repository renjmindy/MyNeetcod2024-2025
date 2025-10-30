from collections import deque

class CafeOrderQueue:
    def __init__(self):
        # TODO: Initialize the order queue using deque
        #pass
        self.order = deque()
    
    def add_order(self, order_id):
        # TODO: Add an order to the queue
        #pass
        self.order.append(order_id)

    def serve_order(self):
        # TODO: Serve (remove) the first order in the queue; raise an exception if there are no orders
        #pass
        if self.order: removed_order = self.order.popleft(); return removed_order
        else: 
            raise Exception
            

# TODO: Initialize an instance of CafeOrderQueue
cafe_order = CafeOrderQueue()

# TODO: Add at least three orders by their ID
cafe_order.add_order(101)
cafe_order.add_order(102)
cafe_order.add_order(103)

# TODO: Serve an order and print the ID of the order served
print(cafe_order.serve_order())
