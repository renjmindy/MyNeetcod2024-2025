from collections import deque

# Initialize a deque with a list of elements
fruit_deque = deque(['Apple', 'Banana', 'Mango', 'Orange'])

# TODO: Rotate the deque so the last element becomes the first
fruit_deque.rotate(1)
# TODO: Print the first element of the deque to verify rotation
print(fruit_deque.popleft())
