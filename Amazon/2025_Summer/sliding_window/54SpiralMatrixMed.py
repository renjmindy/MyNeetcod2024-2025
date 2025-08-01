class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        l, r, t, b = 0, len(matrix[0]), 0, len(matrix)

        ans = list()

        while len(ans) < len(matrix) * len(matrix[0]):

            for j in range(l, r):
                ans.append(matrix[t][j])

            t += 1

            for i in range(t, b):
                ans.append(matrix[i][r - 1])

            r -= 1

            if t < b:
                for j in range(r - 1, l - 1, -1):
                    ans.append(matrix[b - 1][j])

            b -= 1

            if l < r:
                for i in range(b - 1, t - 1, -1):
                    ans.append(matrix[i][l])

            l += 1

        print(ans)

        return ans
