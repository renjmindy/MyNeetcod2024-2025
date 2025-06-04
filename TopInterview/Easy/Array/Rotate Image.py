class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for l in range(len(matrix)):
            for r in range(l):
                matrix[l][r], matrix[r][l] = matrix[r][l], matrix[l][r]
                
        for l in range(len(matrix)):
            matrix[l] = matrix[l][::-1]
