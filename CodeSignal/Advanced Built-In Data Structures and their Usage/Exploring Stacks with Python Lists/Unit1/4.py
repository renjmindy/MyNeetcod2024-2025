# Complete the function to properly use stack operations for parenthesis matching
def is_valid_expression(expression):
    stack = []
    mp = {')':'(', ']':'[', '}':'{'}
    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            # TODO: Determine if the stack is empty OR the last character does not match the corresponding opening character
            if not stack or mp[char] != stack[-1]: return False
            else: stack.pop()
        # TODO: What to do if the `char` is not a parenthesis?
    # TODO: Check if the stack is empty, indicating that the expression is balanced
    return len(stack) == 0  # Modify this line appropriately

# Example usage
sample_expression = "([a+b]{c+d})"
print(is_valid_expression(sample_expression))  # Expected output: True

bad_expression = "([a+b]{c+d}))"
print(is_valid_expression(bad_expression))  # Expected output: False
