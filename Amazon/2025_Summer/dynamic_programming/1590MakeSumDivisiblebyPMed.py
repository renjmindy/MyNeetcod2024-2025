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
