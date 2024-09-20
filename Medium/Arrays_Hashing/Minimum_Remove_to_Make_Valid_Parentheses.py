class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        mp = list()
        sp = list() # sp = set()
        ans = ''

        for i, c in enumerate(s):
            if c == '(': mp.append(i)
            elif c == ')': 
                if mp: mp.pop()
                else: sp.append(i) # sp.add(i)

        #sp.update(mp)
        sp += mp

        for i, c in enumerate(s):
            if i not in sp: ans += c

        return ans
