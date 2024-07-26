class Solution:
    def maxScore(self, s: str) -> int:
        
        ans = 0

        for r in range(1, len(s)):
            ans = max(ans, Counter(s[:r])['0'] + Counter(s[r:])['1'])

        return ans
