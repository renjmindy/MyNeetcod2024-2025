from collections import deque

# Create a deque and perform a sequence of operations
processing_queue = deque(['Task1', 'Task2', 'Task3'])
processing_queue.append('Task4')  # Add new task to the right end
# TODO: Add the highest priority task (Task0) to the beginning of the queue
processing_queue.appendleft('Task0')
# TODO: Process and print the first task in the queue
print(processing_queue.popleft())
