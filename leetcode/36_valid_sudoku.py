# -*- coding: utf-8 -*-

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        return self.rows(board) and self.cols(board) and self.grid(board)

    def check(self, unit):
        tmp = [x for x in unit if x != '.']
        return len(tmp) == len(set(tmp))

    def rows(self, board):
        for row in board:
            if not self.check(row):
                return False 
        return True

    def cols(self, board):
        for col in zip(*board):
            if not self.check(col):
                return False
        return True 

    def grid(self, board):
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                tmp = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.check(tmp):
                    return False
        return True 
    




                
board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]


a = Solution().isValidSudoku(board)
print(a)