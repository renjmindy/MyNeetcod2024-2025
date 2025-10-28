# TODO: Define a function named evaluate_reverse_polish_notation that accepts an expression as a parameter
def evaluate_reverse_polish_notation(exp):
    # TODO: Initialize an empty list to act as the stack
    ans = list()
    tmp = 0
    # TODO: Split the expression into tokens and iterate over them in reverse order
    for c in exp.split():
        # TODO: If the token is an operator ('+', '-'), pop the top two elements from the stack for operation
        if c in ['+', '-']:
            num1 = ans.pop()
            num2 = ans.pop()
            # TODO: Based on the operator, perform the appropriate operation and push the result back onto the stack
            if c == '+': tmp = num1 + num2; ans.append(tmp)
            else: tmp = num2 - num1; ans.append(tmp)
        # TODO: Otherwise, treat the token as an operand and push it onto the stack
        else: ans.append(int(c))
        
    # TODO: Return the top element of the stack as the result of the expression evaluation
    return ans[-1]
# Example usage
expression = "1 2 + 3 -"
print(evaluate_reverse_polish_notation(expression))  # Expected output: 0
