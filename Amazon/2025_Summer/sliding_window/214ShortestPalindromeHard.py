class Solution:
    def shortestPalindrome(self, s: str) -> str:

        if len(s) == 0: return ''

        r = s[::-1]

        for i in range(len(r)):
            if s.startswith(r[i:]): return r[:i] + s
