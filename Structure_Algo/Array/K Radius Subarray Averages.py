class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        ans = [-1] * len(nums)
        win = 2 * k + 1
        
        if len(nums) < 2 * k + 1: return ans
        
        pre = [0] * (len(nums) + 1)
        
        for r in range(len(nums)):
            pre[r + 1] = pre[r] + nums[r]
            
        for r in range(k, len(nums) - k):
            ans[r] = (pre[r + k + 1] - pre[r - k]) // win
            
        return ans
