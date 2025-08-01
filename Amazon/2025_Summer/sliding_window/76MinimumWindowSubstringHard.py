class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        mp = Counter(t)
        ans = ''
        l, cnt = 0, 0

        for r in range(len(s)):
            if mp[s[r]] > 0: cnt += 1
            mp[s[r]] -= 1

            if cnt == len(t):
                while l < len(s) and mp[s[l]] < 0:
                    mp[s[l]] += 1
                    l += 1

                if len(ans) > (r - l + 1) or len(ans) == 0:
                    ans = s[l:r + 1]

        return ans
