class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        ans = s[0]

        for r in range(1, len(s)):
            for l in range(r):
                if len(ans) < len(s[l:r + 1]) and s[l:r + 1] == s[l:r + 1][::-1]:
                    ans = s[l:r + 1]

        return ans
