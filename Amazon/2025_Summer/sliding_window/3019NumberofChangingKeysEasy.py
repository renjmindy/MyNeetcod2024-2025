class Solution:
    def countKeyChanges(self, s: str) -> int:
        
        ans = 0

        for r in range(1, len(s)):
            if s[r - 1].lower() != s[r].lower(): ans += 1

        return ans
