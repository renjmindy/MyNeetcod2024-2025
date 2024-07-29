class Solution:
    def makeGood(self, s: str) -> str:
        
        ans = list()
        ans.append(s[0])

        for i in range(1, len(s)):
            if s[i].isupper():
                if len(ans) and ans[-1] == s[i].lower(): ans.pop()
                else: ans.append(s[i])
            else:
                if len(ans) and ans[-1] == s[i].upper(): ans.pop()
                else: ans.append(s[i])

        return ''.join(ans)
