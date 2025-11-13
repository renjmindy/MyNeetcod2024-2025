class TaskManagementSystem:
    def __init__(self):
        # Store tasks in a dictionary to quickly access them by task_id
        self.tasks = {}
        self.operation_history = []

    def add_task(self, task_id: str, description: str) -> bool:
        if task_id in self.tasks:
            return False
        self.operation_history.append(('add', task_id))
        self.tasks[task_id] = {'description': description, 'priority': None, 'category': None}
        return True

    def edit_task(self, task_id: str, new_description: str) -> bool:
        if task_id not in self.tasks:
            return False
        self.operation_history.append(('edit', task_id, self.tasks[task_id]['description']))
        self.tasks[task_id]['description'] = new_description
        return True

    def remove_task(self, task_id: str) -> bool:
        if task_id not in self.tasks:
            return False
        self.operation_history.append(('remove', task_id, self.tasks[task_id].copy()))
        del self.tasks[task_id]
        return True

    def set_task_priority(self, task_id: str, priority: int) -> bool:
        if task_id not in self.tasks:
            return False
        self.operation_history.append(('priority', task_id, self.tasks[task_id]['priority']))
        self.tasks[task_id]['priority'] = priority
        return True

    def get_tasks_by_priority(self, min_priority: int) -> list:
        return [task_id for task_id, task_info in self.tasks.items() if task_info['priority'] is not None and task_info['priority'] >= min_priority]

    def categorize_task(self, task_id: str, category: str) -> bool:
        if task_id not in self.tasks:
            return False
        self.operation_history.append(('categorize', task_id, self.tasks[task_id]['category']))
        self.tasks[task_id]['category'] = category
        return True

    def get_tasks_by_category(self, category: str) -> list:
        return [task_id for task_id, task_info in self.tasks.items() if task_info['category'] == category]
        
    def undo_last_operation(self) -> bool:
        if len(self.operation_history):
            if self.operation_history[-1][0] == 'add':
                del self.tasks[self.operation_history[-1][1]]
            elif self.operation_history[-1][0] == 'edit':
                self.tasks[self.operation_history[-1][1]]['description'] = self.operation_history[-1][2]
            elif self.operation_history[-1][0] == 'remove':
                self.tasks[self.operation_history[-1][1]] = self.operation_history[-1][2]
            elif self.operation_history[-1][0] == 'priority':
                self.tasks[self.operation_history[-1][1]]['priority'] = self.operation_history[-1][2]
            elif self.operation_history[-1][0] == 'categorize':
                self.tasks[self.operation_history[-1][1]]['category'] = self.operation_history[-1][2]
            self.operation_history.pop() 
            return True
        else: return False
        
    def change_task_category(self, task_id: str, new_category: str) -> bool:
        if task_id in self.tasks:
            self.categorize_task(task_id, new_category)
            return True
        else: return False
