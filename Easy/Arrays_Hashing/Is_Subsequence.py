class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        l = 0

        for r in range(len(t)):
            if l < len(s) and s[l] == t[r]: l += 1

        return l == len(s) if len(s) else l == 0
