
'''

51. N-Queens

Hard
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. 
You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space, respectively.

Work on optimizing this!!!!
Bitmasks?
Faster safe checks?
Can we use a set to track columns and diagonals?


'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for i in range(n)]

        def backtrack(path, r):
            if r == n:
                res.append([''.join(row) for row in board])
                return 

            for c in range(n):
                # check safe
                if self.safe(path, r, c):
                    board[r][c] = 'Q'
                    backtrack(path + [(r,c)], r+1)
                    board[r][c] = '.'
        backtrack([], 0)
        return res 

    def safe(self, path, r, c):
        # check valid cell -> implicit
        # check row and col is valid
        for (x,y) in path:
            if r == x or c == y:
                return False
            if abs(r - x) == abs(c - y):
                return False
        return True

