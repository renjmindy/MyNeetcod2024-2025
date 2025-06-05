class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        for r in range(len(nums)):
            if sum(nums[:r]) == sum(nums[r + 1:]): return r

        return -1
