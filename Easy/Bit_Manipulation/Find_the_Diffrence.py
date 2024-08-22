class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        sc = Counter(s)
        tc = Counter(t)

        for k, v in tc.items(): 
            if k not in sc: return k
            else: 
                if v != sc[k]: return k
