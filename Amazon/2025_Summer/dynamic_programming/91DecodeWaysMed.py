class Solution:
    def numDecodings(self, s: str) -> int:

        if len(s) == 0 or s[0] == '0': return 0
        
        mp = [0] * (len(s) + 1)
        mp[0] = 1
        mp[1] = 1

        for r in range(2, len(s) + 1):
            if 1 <= int(s[r - 1]) <= 9: mp[r] += mp[r - 1]
            if 10 <= int(s[r - 2:r]) <= 26: mp[r] += mp[r - 2]

        return mp[len(s)]
