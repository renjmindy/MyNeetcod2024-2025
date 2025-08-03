class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        mp = defaultdict(int)

        for r in range(len(s) - 9):
            mp[s[r : r + 10]] += 1

        return [k for k, v in mp.items() if v > 1]
