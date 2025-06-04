class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ans = list()
        
        for l in range(len(board)):
            for r in range(len(board[0])):
                if board[l][r] != '.':
                    ans.extend([(l, board[l][r]), (board[l][r], r), (l // 3, r // 3, board[l][r])])
                
        return len(set(ans)) == len(ans)
