class Solution:
    def scoreOfString(self, s: str) -> int:
        
        ans = 0
        for a, b in zip(map(ord, s), map(ord, s[1:])): ans += abs(a - b)

        return ans
