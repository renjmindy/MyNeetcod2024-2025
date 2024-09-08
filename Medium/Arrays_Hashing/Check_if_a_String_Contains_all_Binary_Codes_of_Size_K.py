class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        counts = 2 ** k
        ans = set()

        for i in range(len(s) - k + 1):
            if s[i:i+k] not in ans:
                ans.add(s[i:i+k])
                counts -= 1
                if counts == 0: return True

        return counts == 0
