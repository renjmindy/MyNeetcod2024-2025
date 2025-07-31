class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2): return False

        n1 = Counter(s1)
        n2 = Counter(s2[:len(s1)]) # set same length as s1

        if n1 == n2: return True

        for r in range(len(s1), len(s2)):
            n2[s2[r]] += 1 # add one more letter on the right
            n2[s2[r - len(s1)]] -= 1 # drop one more letter on the left

            if n2[s2[r - len(s1)]] == 0: del n2[s2[r - len(s1)]]

            if n1 == n2: return True

        return False
