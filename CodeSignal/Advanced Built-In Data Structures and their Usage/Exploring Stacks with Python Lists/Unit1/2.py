# Define a function to check for the next available tray without removing it
def next_tray(stack):
    # TODO: Return the top-most tray without removing it from the stack
    if stack: return stack[-1]
    else: return "No trays available."

# Initialize the stack with tray IDs
tray_stack = [1001, 1002, 1003]

# TODO: Use the `next_tray` function to check and print which tray will be served next
print(f"next tray before removal: {next_tray(tray_stack)}")
# Simulate removing a tray from the stack
tray_stack.pop()

# TODO: Use the `next_tray` function to check and print the next tray after one is removed
print(f"next tray after removal: {next_tray(tray_stack)}")
