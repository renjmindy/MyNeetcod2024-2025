class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        
        if sum(machines) % len(machines): return -1

        cost = sum(machines) // len(machines)

        ans, dif = 0, 0

        for r in range(len(machines)):
            dif += machines[r] - cost
            # The maximum value of abs(dif) indicates the 
            # maximum number of steps that needs to be 
            # moved in a single move
            ans = max(ans, abs(dif), machines[r] - cost)

        return ans
