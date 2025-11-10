from collections import defaultdict
from typing import List, Optional

class TaskTrackingSystem:
    def __init__(self):
        self.tasks = {}
        self.task_attributes = defaultdict(dict)
        self.dependency = defaultdict(set)
        self.dependents = defaultdict(set)

    def add_task(self, task_id: str, title: str, description: str, status: str, priority: int) -> bool:
        if task_id in self.tasks:
            return False
        self.tasks[task_id] = True
        self.task_attributes[task_id] = {
            'title': title,
            'description': description,
            'status': status,
            'priority': priority
        }
        return True

    def update_task(self, task_id: str, title: Optional[str] = None, description: Optional[str] = None, status: Optional[str] = None, priority: Optional[int] = None) -> bool:
        if task_id not in self.tasks:
            return False
        if title is not None:
            self.task_attributes[task_id]['title'] = title
        if description is not None:
            self.task_attributes[task_id]['description'] = description
        if status is not None:
            self.task_attributes[task_id]['status'] = status
        if priority is not None:
            self.task_attributes[task_id]['priority'] = priority
            
        if status == "Closed":
            for dependent in self.dependents[task_id]:
                if all(self.task_attributes[dep]['status'] == 'Closed' for dep in self.dependency[dependent]): self.task_attributes[dependent]['status'] = "Open"    
            
        return True

    def remove_task(self, task_id: str) -> bool:
        if task_id in self.tasks:
            for dependent in self.dependents[task_id]: self.dependency[dependent].remove(task_id)
            for dependency in self.dependency[task_id]: self.dependents[dependency].remove(task_id)
            del self.dependency[task_id]
            del self.dependents[task_id]
            del self.tasks[task_id]
            del self.task_attributes[task_id]
            return True
        return False

    def get_tasks_by_status(self, status: str) -> List[str]:
        return sorted([task_id for task_id, attrs in self.task_attributes.items() if attrs['status'] == status])

    def get_tasks_by_priority(self, priority: int) -> List[str]:
        return sorted([task_id for task_id, attrs in self.task_attributes.items() if attrs['priority'] == priority])
        
    def has_path(self, start, target, visited=None):
        if visited is None: visited = set()
        if start == target: return True
        visited.add(start)
        for neighbor in self.dependency.get(start, set()):
            if neighbor not in visited: 
                if self.has_path(neighbor, target, visited): return True
        return False     
        
    def add_dependency(self, task_id: str, dependency_task_id: str) -> bool:
        if task_id != dependency_task_id and task_id in self.tasks and dependency_task_id in self.tasks:
            if task_id not in self.dependents[dependency_task_id] and not self.has_path(dependency_task_id, task_id):
                self.dependents[dependency_task_id].add(task_id)
                self.dependency[task_id].add(dependency_task_id)
                return True
        return False
        
    def remove_dependency(self, task_id: str, dependency_task_id: str) -> bool:
        if task_id not in self.dependents[dependency_task_id] or dependency_task_id not in self.dependency[task_id]: return False
        
        if task_id in self.dependents[dependency_task_id]: 
            self.dependents[dependency_task_id].remove(task_id)
        if dependency_task_id in self.dependency[task_id]:
            self.dependency[task_id].remove(dependency_task_id)
        return True
        
    def get_dependent_tasks(self, task_id: str) -> List[str]:
        return sorted(list(self.dependents[task_id]))
