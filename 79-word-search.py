class Solution:
    '''
    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(r, c, k):
            # if k is end of length word, all matches found
            if k == len(word):
                return True 

            # check valid cell and match
            if r < 0 or r >= n or c < 0 or c >= m or board[r][c] != word[k]:
                return False 

            # Ensure that there are no infinite loops or reused cells
            # At each level, hold a tmp variable and mark the cell
            tmp = board[r][c]
            board[r][c] = "#"

            # backtrack deeper, only need single true
            if backtrack(r+1,c, k+1) or backtrack(r-1, c, k+1) or backtrack(r, c+1, k+1) or backtrack(r, c-1, k+1):
                return True 

            # after exhausting options at current cell, reset cell, return False 
            board[r][c] = tmp
            return False

        n, m = len(board), len(board[0])
        for r in range(n):
            for c in range(m):
                if backtrack(r,c, 0):
                    return True
        return False 