class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        v1 = version1.split('.')
        v2 = version2.split('.')

        for r in range(max(len(v1), len(v2))):
            if r > len(v1) - 1: v1val = 0
            else: v1val = int(v1[r])
            if r > len(v2) - 1: v2val = 0
            else: v2val = int(v2[r])

            if v1val > v2val: return 1
            elif v1val < v2val: return -1

        return 0
