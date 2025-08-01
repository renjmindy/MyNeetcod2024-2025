class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if sum(nums) < target: return 0

        ans, l, pre = len(nums), 0, 0

        for r in range(len(nums)):
            pre += nums[r]
            while pre >= target:
                print(r, l, pre)
                ans = min(ans, r - l + 1)
                pre -= nums[l]
                l += 1
                

        return ans
