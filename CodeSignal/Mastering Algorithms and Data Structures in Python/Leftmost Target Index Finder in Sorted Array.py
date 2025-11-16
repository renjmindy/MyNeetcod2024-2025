def insert_position(nums, target):
    # implement this
    # pass
    nums.append(float('inf'))  # append an infinite element to handle edge case
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left + 1) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

print(insert_position([1, 2, 3, 3, 5], 3))  # Expected output: 2
print(insert_position([1, 2, 3, 3, 5], 4))  # Expected output: 4
print(insert_position([1, 3, 5, 7, 9], 10)) # Expected output: 5
