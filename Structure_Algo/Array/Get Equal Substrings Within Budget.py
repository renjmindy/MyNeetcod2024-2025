class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        l, pre, ans = 0, 0, 0

        for r in range(len(s)):
            pre += abs(ord(s[r]) - ord(t[r]))

            while pre > maxCost:
                pre -= abs(ord(s[l]) - ord(t[l]))
                l += 1

            ans = max(ans, r - l + 1)

        return ans
