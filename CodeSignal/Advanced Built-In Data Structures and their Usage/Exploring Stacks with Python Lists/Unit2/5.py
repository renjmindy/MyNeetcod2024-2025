from collections import deque

# TODO: Create a deque for coffee shop orders with initial orders 'Latte', 'Espresso', 'Cappuccino'
d = deque(['Latte', 'Espresso', 'Cappuccino'])
# TODO: A new customer orders a 'Mocha', add it to the end of the queue
d.append('Mocha')
# TODO: Realize a customer wants their 'Latte' order moved to the end of the queue. Implement it.
d.rotate(-1)
# TODO: Process (remove and print) the first order in the queue. Which drink is it?
first_order = d.popleft()
print(first_order)
