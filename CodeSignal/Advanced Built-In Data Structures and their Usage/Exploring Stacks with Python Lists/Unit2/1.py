from collections import deque

# Simulate a supermarket checkout queue using a deque
checkout_line = deque(['Person1', 'Person2', 'Person3'])
checkout_line.append('Person4')  # Person4 joins the end of the line
serviced_customer = checkout_line.popleft()  # Processing the first customer

print(serviced_customer)  # Unexpectedly shows 'Person4'
