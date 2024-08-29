class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ans = list()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    ans.extend([(i, board[i][j]), (board[i][j], j), (i // 3, j // 3, board[i][j])])

        return len(ans) == len(set(ans))
