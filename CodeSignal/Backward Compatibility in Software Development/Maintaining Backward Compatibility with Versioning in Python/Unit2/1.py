class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, priority, urgent=False):
        # TODO: Modify this method to support an 'urgent' parameter with a default value of False.
        # If a task is 'urgent', add it to the beginning of the list.
        if urgent:
            self.tasks.insert(0, {'name': task_name, 'priority': priority, 'urgent': urgent})
        else:
            if len(self.tasks) >= 100:
                raise ValueError("Maximum task limit reached.")
            if not 1 <= priority <= 5:
                raise ValueError("Priority must be between 1 and 5.")
            if len(task_name) > 50:
                raise ValueError("Task name exceeds 50 characters.")

            self.tasks.append({'name': task_name, 'priority': priority, 'urgent': urgent})

    def get_tasks(self):
        return self.tasks
