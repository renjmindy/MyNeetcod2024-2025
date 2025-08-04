class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tot = sum(nums)
        rem = tot % p

        if rem == 0: return 0

        ans, pre, mp = len(nums), 0, defaultdict(int) # trick: upper bound of ans is the overall length of array
        mp[0] = -1

        for r in range(len(nums)):
            pre += nums[r]

            ans_rem = (pre % p - rem) % p

            if ans_rem in mp: ans = min(ans, r - mp[ans_rem])

            mp[pre % p] = r

        return ans if ans < len(nums) else -1 


-----------------------------------------------------------------------------------------------------------------------------

total = sum(nums)
        rem = total % p

        if rem == 0: return 0

        mp = defaultdict(int)
        mp[0] = -1
        pre = 0
        ans = len(nums)

        for r in range(len(nums)):
            pre += nums[r]
            mod = ((pre % p) - rem + p) % p

            if mod in mp:
                ans = min(ans, r - mp[mod])

            mp[pre % p] = r

        return ans if ans < len(nums) else -1
