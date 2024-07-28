class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l, r = 1, 0

        while r < len(nums):
            if nums[l - 1] != nums[r]: nums[l], nums[r] = nums[r], nums[l]; l += 1 
            r += 1
                
        return l
