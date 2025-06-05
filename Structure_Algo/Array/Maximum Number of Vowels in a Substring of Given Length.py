class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vlist = ['a', 'e', 'i', 'o', 'u']

        l, pre, ans = 0, 0, 0

        mp = defaultdict(int)

        for r in range(k):
            if s[r] in vlist: pre += 1; mp[s[r]] += 1
            
        ans = pre

        for r in range(k, len(s)):
            if s[r] in vlist: pre += 1; mp[s[r]] += 1
            if s[l] in vlist: pre -= 1; mp[s[l]] -= 1
            l += 1
            ans = max(ans, pre)
            

        return ans
