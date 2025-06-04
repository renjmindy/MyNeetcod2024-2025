class Solution:
    def reverseWords(self, s: str) -> str:
        
        ans = ''

        for t in s.split(' '):
            ans += t[::-1]
            ans += ' '

        return ans[:-1]
