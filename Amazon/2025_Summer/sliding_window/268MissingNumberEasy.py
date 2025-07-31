class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()

        for r in range(len(nums)):
            if r != nums[r]: return r

        return len(nums) 
