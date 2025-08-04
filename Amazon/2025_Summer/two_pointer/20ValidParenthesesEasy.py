class Solution:
    def isValid(self, s: str) -> bool:
        
        mp = {')':'(', '}':'{', ']':'['}
        ans = list()
        
        for c in s:
            if c not in mp: ans.append(c)
            else:
                if len(ans) == 0 or ans[-1] != mp[c]: return False
                else:
                    ans.pop()
                    
        return len(ans) == 0
