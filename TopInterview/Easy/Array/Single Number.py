class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        check = 0
        
        for r in range(len(nums)):
            check ^= nums[r]
            print(check)
            
        return check 
