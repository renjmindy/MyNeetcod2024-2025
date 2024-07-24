class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        for l in range(len(nums)):
            if sum(nums[:l]) == sum(nums[l + 1:]): return l

        return -1
