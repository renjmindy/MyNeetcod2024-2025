class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        ans = 0

        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] + nums[r] > target: r -= 1
            else: 
                ans += 2 ** (r - l)
                ans %= (10 ** 9 + 7)
                l += 1

        ans %= (10 ** 9 + 7)
        return ans
