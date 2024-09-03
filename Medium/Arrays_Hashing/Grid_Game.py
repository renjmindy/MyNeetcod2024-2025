class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        first_row_sum = sum(grid[0])
        second_row_sum = 0
        ans = math.inf

        for col in range(len(grid[0])):
            first_row_sum -= grid[0][col]
            ans = min(ans, max(first_row_sum, second_row_sum))
            second_row_sum += grid[1][col]

        return ans
