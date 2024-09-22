class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        pre_balloon, pre_time = colors[0], neededTime[0]
        ans = 0

        for r in range(1, len(colors)):
            if pre_balloon == colors[r]:
                if pre_time < neededTime[r]:
                    ans += pre_time
                    pre_time = neededTime[r]
                else:
                    ans += neededTime[r]
            else:
                pre_time = neededTime[r]
                pre_balloon = colors[r]

        return ans
