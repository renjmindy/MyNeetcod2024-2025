class Solution:
    def canJump(self, nums: List[int]) -> bool:

        mp = [0] * len(nums)
        mp[0] = nums[0]

        for r in range(1, len(nums)):
            if mp[r - 1] < r: return False
            mp[r] = max(mp[r - 1], r + nums[r])

        print(mp)

        return mp[-1] >= (len(nums) - 1)
