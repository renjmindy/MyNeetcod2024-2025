class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        ans = [[0] * (len(grid[0]) - 2) for _ in range((len(grid) - 2))]
        print(ans)

        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                cur = 0
                for k in range(3):
                    for l in range(3):
                        cur = max(cur, grid[i + k][j + l])
                ans[i][j] = cur

        return ans
