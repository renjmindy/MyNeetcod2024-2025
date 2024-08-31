class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        pre, ans = 0, 0
        mp = defaultdict(int)
        mp[0] = 1

        for r in range(len(nums)):
            pre += nums[r]
            if pre - k in mp: ans += mp[pre - k] 
            mp[pre] += 1

        return ans
