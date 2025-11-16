# Python program to find the value of 'x' when f(x) = 0 using Binary Search on Continuous Space
import math

# Define a continuous function 'f'
def f(x):
    return x**3 - 5 * x**2 + 5

# TODO: Write the Binary Search Function that performs the search on the continuous function in the interval [2, 5]
# Binary Search Function
def binary_search(func, target, left, right, epsilon):
    while right - left > epsilon:
        middle = (left + right) / 2
        if func(middle) > target:
            left = middle
        else:
            right = middle        
    return middle

# TODO: Define precision, target value, and interval bounds
epsilon = 1e-6  # to make sure the solution is within an acceptable range
target = 0  # target f(x) value
start = 2  # starting point of the interval
end = 5  # ending point of the interval

# TODO: Implement the binary search function and print out the value of 'x' for which f(x) is approximately 0.
result = binary_search(f, target, start, end, epsilon)
print("The value of x for which f(x) is approximately 0 is: ", result)
