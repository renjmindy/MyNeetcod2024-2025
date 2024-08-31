class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        cp = Counter(s)
        mp = {k:v for k, v in cp.items() if v > 1}

        ans = 0

        for k, v in mp.items():
            ans += len(set(s[s.find(k) + 1:s.rfind(k)]))

        return ans
