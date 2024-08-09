class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while True:

            if len(stones) == 1: return stones[0]
            elif len(stones) == 0: return 0

            stones.sort()
            stones = stones[::-1]

            s1 = stones.pop(0)
            s2 = stones.pop(0)
            if s1 == s2: continue
            else: stones.append(s1 - s2)
