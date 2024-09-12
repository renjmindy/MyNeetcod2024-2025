class Solution:
    def partitionString(self, s: str) -> int:
        
        sp = set()
        ans = 0

        for c in s:
            if c not in sp: sp.add(c)
            else: ans += 1; sp.clear(); sp.add(c)

        return ans + 1
