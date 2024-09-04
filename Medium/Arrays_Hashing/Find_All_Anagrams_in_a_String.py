class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s): return []

        sc, pc = defaultdict(int), defaultdict(int)
        ans = []

        for i in range(len(p)):
            sc[s[i]] += 1
            pc[p[i]] += 1

        if sc == pc: ans.append(0)

        l = 0

        for r in range(len(p), len(s)):
            sc[s[r]] += 1
            sc[s[l]] -= 1
            if sc[s[l]] == 0: sc.pop(s[l])
            l += 1
            if sc == pc: ans.append(l)

        return ans 
