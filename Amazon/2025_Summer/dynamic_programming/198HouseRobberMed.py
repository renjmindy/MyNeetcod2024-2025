class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 2: return max(nums)

        mp = [0] * len(nums)

        mp[0] = nums[0]
        mp[1] = max(nums[0], nums[1])

        for r in range(2, len(nums)):
            mp[r] = max(mp[r - 1], nums[r] + mp[r - 2])

        return mp[-1]
