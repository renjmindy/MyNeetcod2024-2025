class Solution:
    def scoreOfString(self, s: str) -> int:
        
        ans = 0

        for r in range(1, len(s)):
            ans += abs(ord(s[r]) - ord(s[r - 1]))

        return ans
