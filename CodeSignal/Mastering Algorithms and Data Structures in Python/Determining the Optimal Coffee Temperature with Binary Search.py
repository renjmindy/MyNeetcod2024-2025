# Python program to find the temperature at which a specific coffee type is approximated to be best
import math

# Define the continuous function for the specific coffee type  
def coffee_function(T):
    return -((T - 85)**2) + 60

# Define the binary search function 
def binary_search(func, target, left, right, precision):
    while right - left > precision:
        mid = (left + right) / 2
        # TODO: Update `left` and `right` bounds based on the `func(mid)` value
        if coffee_function(mid) > target: right = mid
        else: left = mid
    return (left + right) / 2

# Requested precision
epsilon = 1e-6
# Identify the temperature range in which the coffee tastes the best 
temperature_range = [30, 100]

# TODO: Find the exact temperature at which your coffee tastes best.
epsilon = 1e-6  # to make sure the solution is within an acceptable range
target = 30  # target f(x) value
start = 30  # starting point of the interval
end = 100  # ending point of the interval

result = binary_search(coffee_function, target, start, end, epsilon)
print("The value of x for which f(x) is approximately 30 is: ", result)
