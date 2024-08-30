class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        ans = defaultdict(int)

        for i in range(len(wall)):
            for j in accumulate(wall[i]):
                ans[j] += 1

        return len(wall) - max([v for k, v in ans.items() if 0 < k < sum(wall[0])], default=0)
