def search_dec_rotated(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid 
        if nums[right] <= nums[mid] and nums[right] <= target < nums[mid]:
            left = mid + 1
        elif nums[mid] <= nums[left] and nums[mid] < target <= nums[left]:
            right = mid - 1
        elif nums[mid] > nums[left]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

print(search_dec_rotated([4, 3, 2, 1, 8, 7, 6, 5], 1))  # Expected output: 3
print(search_dec_rotated([9, 8, 7, 6, 5, 4, 3, 2, 1], 4))  # Expected output: 5
print(search_dec_rotated([5, 4, 3, 2, 1], 8))  # Expected output: -1
