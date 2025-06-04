class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        pre, ans = 0, 1
        
        for r in range(len(nums)):
            pre += nums[r]
            ans = max(ans, 1 - pre)
            
        return ans
