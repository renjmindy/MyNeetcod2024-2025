def recursiveSumEven(arr, idx=0):
    # implement this
    # pass 
    if idx == len(arr): return 0
    else: return arr[idx] + recursiveSumEven(arr, idx + 2)
        

# Testing the function
print(recursiveSumEven([1, 2, 3, 4, 5, 6])) # Expected output: 9
print(recursiveSumEven([2, 3])) # Expected output: 2
print(recursiveSumEven([])) # Expected output: 0
