# Create a function that determines the minimum number of bracket removals needed for a valid string.
def min_removals_to_balance(brackets):
    # TODO: Initialize an empty list to act as the stack
    ans = list()
    # TODO: Iterate through each bracket in the input string
    for c in brackets:
        # TODO: Add conditions to handle the opening and closing brackets appropriately using stack operations
        if not ans: ans.append(c)
        else:
            if ans[-1] == '(' and c == ')': ans.pop()
            else: ans.append(c)
    # TODO: Return the count of brackets that need to be removed to make the string valid
    return len(ans)
# Example usage
invalid_parentheses = "()))(()"
removals_needed = min_removals_to_balance(invalid_parentheses)
print(removals_needed)  # Expected output: 3
