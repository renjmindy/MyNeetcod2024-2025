class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if sum(nums) < target: return 0

        l, pre, ans = 0, 0, len(nums)

        for r in range(len(nums)):
            pre += nums[r]
            while pre >= target:
                ans = min(ans, r - l + 1)
                pre -= nums[l]
                l += 1

        return ans
