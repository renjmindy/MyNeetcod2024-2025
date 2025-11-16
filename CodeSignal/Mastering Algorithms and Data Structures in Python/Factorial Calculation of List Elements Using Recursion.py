def factorial(num):
    #  Implement this function according to the task description
    # pass
    if num == 0: return 1
    elif num < 0: return "Error"
    else: return num * factorial(num - 1)


def factorials(nums):
    results = []
    for num in nums:
        f = factorial(num)
        if f is not None:
            results.append(f)
        else:
            results.append('Error')
    return results


print(factorials([2, 3, 4]))  # Should print: [2, 6, 24]
print(factorials([1, 5, 6]))  # Should print: [1, 120, 720]
print(factorials([0, -3, 10]))  # Should print: [1, 'Error', 3628800]
