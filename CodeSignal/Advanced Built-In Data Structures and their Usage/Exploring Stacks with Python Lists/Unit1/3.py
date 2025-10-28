class CafeteriaStack:
    def __init__(self):
        self.tray_stack = []  # Stack to hold trays
        
    def add_tray(self, tray_id):
        # TODO: Add a new tray to the stack, considering the LIFO principle
        self.tray_stack.append(tray_id)
        
    def remove_tray(self):
        # TODO: Remove a tray from the stack following the LIFO principle and return it
        if self.tray_stack: removed_element = self.tray_stack[-1]; self.tray_stack.pop(); return removed_element
        return None  # If the stack is empty, nothing to pop

# Simulating cafeteria tray management
cafeteria = CafeteriaStack()
cafeteria.add_tray(101)
cafeteria.add_tray(102)
cafeteria.add_tray(103)
print(cafeteria.remove_tray())  # This should print the number of the last tray added
