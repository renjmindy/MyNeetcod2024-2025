class CafeteriaStack:
    def __init__(self):
        self.stack = []
    
    def add_tray(self, tray_id):
        self.stack.append(tray_id)
    
    def remove_tray(self):
        if self.stack:  # Simplified check for an empty stack
            return self.stack.pop()
        else: print('there are no more trays to remove')

# Sample usage
cafeteria = CafeteriaStack()
cafeteria.add_tray("Tray_4")  # Adding a tray to the stack
print(cafeteria.remove_tray())  # This should print "Tray_4"
print(cafeteria.remove_tray()) # Prints: "No more trays!"
