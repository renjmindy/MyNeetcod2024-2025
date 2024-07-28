class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        slist, tlist = list(), list()

        for r in range(len(s)):
            if s[r] != '#': slist.append(s[r])
            else: 
                if slist: slist.pop()

        for r in range(len(t)):
            if t[r] != '#': tlist.append(t[r])
            else: 
                if tlist: tlist.pop()

        return ''.join(slist) == ''.join(tlist)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        l, r = len(s) - 1, len(t) - 1
        ss, st = 0, 0

        while l >= 0 or r >= 0:
            while l >= 0:
                if s[l] == '#': ss += 1; l -= 1
                elif ss: ss-= 1; l -= 1
                else: break
            while r >= 0:
                if t[r] == '#': st += 1; r -= 1
                elif st: st -= 1; r -= 1
                else: break

            if l >= 0 and r >= 0 and s[l] != t[r]: return False
            if (l >= 0) != (r >= 0): return False

            l -= 1
            r -= 1
        
        return True
