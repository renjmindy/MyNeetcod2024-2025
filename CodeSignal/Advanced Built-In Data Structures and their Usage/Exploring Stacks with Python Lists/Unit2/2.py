from queue import Queue

# Initialize a queue and add elements
morning_tasks = Queue()
morning_tasks.put("Brush Teeth")
morning_tasks.put("Have Breakfast")
morning_tasks.put("Pack Bag")

# TODO: Remove the first task upon its completion
first_task = morning_tasks.get()
second_task = morning_tasks.get()
third_task = morning_tasks.get()

# TODO: Print the first task to confirm it's the correct one being removed
print(first_task)
