import random

# TODO: Define the 'quick_sort_desc' and 'partition_desc' functions to implement Quick Sort in descending order
def partition(arr, low, high):
    # this method partitions arr[low..high] to move all elements <= arr[high] to the left
    # and returns the index of `pivot` in the updated array
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
        
# Generate a list of 20 random numbers between 50 and 100
random_numbers = [random.randint(50, 100) for _ in range(20)]
print("Unsorted List: ", random_numbers)

# TODO: Use the Quick Sort function to sort the list in descending order and print the sorted list
quick_sort(random_numbers, 0, len(random_numbers) - 1)
print('Sorted list with Quick Sort:', random_numbers)
