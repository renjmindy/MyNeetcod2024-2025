class Solution:
    def isValid(self, s: str) -> bool:
        
        mp = {')':'(', '}':'{', ']':'['}
        ans = list()

        for c in s:
            if c not in mp: ans.append(c)
            else:
                if len(ans) and ans[-1] == mp[c]: ans.pop()
                else: return False

        return len(ans) == 0
