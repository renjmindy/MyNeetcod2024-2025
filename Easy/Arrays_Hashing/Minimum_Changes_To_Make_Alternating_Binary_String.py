class Solution:
    def minOperations(self, s: str) -> int:
        
        anse, anso = 0, 0

        for i, c in enumerate(s):
            if i % 2 == int(c): anse += 1
            else: anso += 1

        return min(anse, anso)
