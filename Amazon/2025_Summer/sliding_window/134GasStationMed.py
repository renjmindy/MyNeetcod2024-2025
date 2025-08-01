class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost): return -1

        ans, dif = 0, 0

        for r in range(len(gas)):
            dif += gas[r] - cost[r]
            if dif < 0: dif = 0; ans = r + 1

        return ans
