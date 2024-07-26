class Solution:
    def minOperations(self, s: str) -> int:
        
        ans = 0

        for i, c in enumerate(s):
            if i % 2 == int(c): ans += 1

        return min(ans, 1 - ans)
