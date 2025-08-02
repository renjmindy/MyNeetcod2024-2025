class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        mp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        ans = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    if matrix[i][j] == '1': 
                        mp[i][j] = 1 
                        ans = max(ans, mp[i][j])
                else:
                    if matrix[i][j] == '1':
                        mp[i][j] = 1 + min(mp[i - 1][j], mp[i][j - 1], mp[i - 1][j - 1])
                        ans = max(ans, mp[i][j])

        return ans ** 2

