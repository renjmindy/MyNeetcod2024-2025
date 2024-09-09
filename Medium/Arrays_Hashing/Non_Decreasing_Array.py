class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        found = False

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]: 
                if found: return False
                else: found = True
                if i >= 2 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1] 

        return True 
            
