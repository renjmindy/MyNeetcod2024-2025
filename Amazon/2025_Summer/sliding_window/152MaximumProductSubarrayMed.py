class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        curmax, curmin, ans = nums[0], nums[0], nums[0]

        for r in range(1, len(nums)):
            if nums[r] < 0:
                curmin, curmax = curmax, curmin

            curmax = max(nums[r], nums[r] * curmax)
            curmin = min(nums[r], nums[r] * curmin)

            ans = max(ans, curmax)

        return ans
