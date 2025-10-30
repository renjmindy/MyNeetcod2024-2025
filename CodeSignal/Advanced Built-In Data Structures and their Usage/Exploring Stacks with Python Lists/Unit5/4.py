from sortedcontainers import SortedDict
import datetime

# TODO: Define the Task class with a constructor to initialize its title and due_date
# Make sure to implement the __lt__ method to compare tasks based on due_date
class Task:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
    def __lt__(self, other):
        return self.due_date < other.due_date

# TODO: Create the TaskScheduler class
# It should initialize a SortedDict to hold tasks
class TaskScheduler:
    def __init__(self):
        # Initializing an empty queue
        self.task_bag = SortedDict()
    
# Include methods to schedule a task and get the next task based on due dates
    def schedule_task(self, Task):
        self.task_bag[Task.due_date] = Task.title

    def get_next_task(self):
        if self.task_bag:
            return self.task_bag.peekitem(0)
        else:
            "No more tasks to schedule!"
        
# Initialize TaskScheduler and add tasks
scheduler = TaskScheduler()
task1 = Task('mindy', datetime.date(2025, 10, 31))
task2 = Task('john', datetime.date(2025, 11, 30))

# TODO: Add tasks using the scheduler. Remember to create Task instances with a title and due date
scheduler.schedule_task(task1)
scheduler.schedule_task(task2)

# TODO: Retrieve and print the next task from the scheduler
print(scheduler.get_next_task())
