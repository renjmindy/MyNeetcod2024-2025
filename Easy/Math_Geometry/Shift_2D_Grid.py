class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        mp = [0] * len(grid) * len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                mp[i * len(grid[0]) + j] = grid[i][j]

        mp = mp[-k % (len(grid) * len(grid[0])):] + mp[:-k % (len(grid) * len(grid[0]))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = mp[i * len(grid[0]) + j]

        return grid
