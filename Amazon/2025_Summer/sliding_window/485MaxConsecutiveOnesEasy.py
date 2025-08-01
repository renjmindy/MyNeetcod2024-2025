class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        cnt, ans = 0, 0

        for r in range(len(nums)):
            if nums[r] == 1: cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 0

        ans = max(ans, cnt)

        return ans
