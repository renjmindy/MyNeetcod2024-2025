# Implementation of Binary Search on a specific use case

# List of sorted word lengths in a dictionary
word_lengths = [i for i in range(1, 501)]  # Lengths from 1 to 500

# TODO: Implement the recursion-based binary_search_recursive method
def binary_search_recursive(data, target, low, high):
    #pass
    
    high -= 1
    
    if low == high: return low if data[low] == target else None
    
    pivot = low + (high - low + 1) // 2
    
    if data[pivot] < target:
        return binary_search_recursive(data, target, pivot + 1, high)
    else:
        return binary_search_recursive(data, target, low, pivot - 1)

# Suppose there is a spelling bee, and a contestant is given a word.
# The contestant knows the word is in the dictionary, so let's find what position the length of this word would hold in our sorted list of word lengths
word_length_query = 237
result = binary_search_recursive(word_lengths, word_length_query, 0, len(word_lengths))
if result is not None:
    print(f"Words of length {word_length_query} are found at position {result} in the word lengths list.")
else:
    print(f"No words are found with length {word_length_query}.")

# Implementation of Binary Search on a specific use case

# List of sorted word lengths in a dictionary
word_lengths = [i for i in range(1, 501)]  # Lengths from 1 to 500

# TODO: Implement the recursion-based binary_search_recursive method
def binary_search_recursive(data, target, low, high):
    #pass
    high = high - 1
    
    while low <= high:
        pivot = low + (high - low + 1) // 2
        if data[pivot] < target: low = pivot + 1
        elif data[pivot] > target: high = pivot - 1
        else: return pivot

# Suppose there is a spelling bee, and a contestant is given a word.
# The contestant knows the word is in the dictionary, so let's find what position the length of this word would hold in our sorted list of word lengths
word_length_query = 237
result = binary_search_recursive(word_lengths, word_length_query, 0, len(word_lengths))
if result is not None:
    print(f"Words of length {word_length_query} are found at position {result} in the word lengths list.")
else:
    print(f"No words are found with length {word_length_query}.")

