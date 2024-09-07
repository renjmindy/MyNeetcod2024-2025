class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        sp = set()
        ans = list()

        for i in range(len(s) - 9):
            if s[i:i+10] not in sp: sp.add(s[i:i+10])
            else: ans.append(s[i:i+10])

        return list(set(ans))
