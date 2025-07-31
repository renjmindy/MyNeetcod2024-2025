class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans, pre = -math.inf, -math.inf

        for r in range(len(nums)):
            pre = max(pre + nums[r], nums[r])
            ans = max(ans, pre)

        return ans
