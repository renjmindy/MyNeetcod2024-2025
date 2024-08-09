class Solution:
    def help(self, x, y, grid):

        if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]) or grid[x][y] == 0: return 1
        if grid[x][y] == -1: return 0
        grid[x][y] = -1

        return self.help(x + 1, y, grid) + self.help(x - 1, y, grid) + self.help(x, y + 1, grid) + self.help(x, y - 1, grid) 

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: ans = self.help(i, j, grid)

        return ans
