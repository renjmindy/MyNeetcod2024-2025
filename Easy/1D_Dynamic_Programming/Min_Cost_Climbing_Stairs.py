class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        pre, cur = 0, 0

        for r in range(len(cost)):
            pre, cur = cur, min(pre + cost[r], cur + cost[r])

        return min(pre, cur)
