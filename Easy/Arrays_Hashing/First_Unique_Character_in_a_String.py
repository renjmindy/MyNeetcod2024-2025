class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        cp = Counter(s)
        ans = math.inf

        for k, v in cp.items():
            if v == 1: ans = min(ans, s.index(k))

        return ans if ans < math.inf else -1
