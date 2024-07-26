class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        if len(s) == len(set(s)): return -1

        mp = defaultdict(int)

        ans = 0

        for r in range(len(s)):
            if s[r] in mp:
                ans = max(ans, (r - mp[s[r]] - 1))
            else: mp[s[r]] = r

        return ans
