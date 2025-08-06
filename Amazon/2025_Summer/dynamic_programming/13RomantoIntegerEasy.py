class Solution:
    def romanToInt(self, s: str) -> int:
        
        mp = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        ans = mp[s[-1]]

        for r in range(len(s) - 2, -1, -1):
            if mp[s[r]] >= mp[s[r + 1]]: ans += mp[s[r]]
            else: ans -= mp[s[r]]

        return ans
