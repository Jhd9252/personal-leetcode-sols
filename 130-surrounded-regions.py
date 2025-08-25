class Solution:
    '''
    The intuition is that we want to turn all captured O's into X's. 
    There are two classifications of O's, safe and unsafe. 

    One method is begin traversal at all O's and find out if the region is unsafe. 
    We can't make the mistake of local truths, if using DFS -> on stack is not TRUE. 
    We would have to have a variable called region (hold all O cells), and surrounded (bool).
    After the return, we would turn all cells in region var to X if surrounded == True. 

    Another method, is to focus on the safe O's. Safe O's are regions that start at the border. Any 
    other O cell that is a neighbor is safe. Thus, after hiding those safe cells, we flip the unsafe O cells, 
    before revealing the safe cells. 

    '''
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        safe = set()
        dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]

        def check (r, c):
            if r < 0 or r >= n or c < 0 or c >= m or board[r][c] == 'X' or (r,c) in safe:
                return False
            # in bounds, is O-cell, not visited
            return True 

        def dfs(r, c, safe):
            safe.add((r,c))
            for dx, dy in dirs:
                nr, nc = r + dx, c + dy
                if check(nr, nc):
                    dfs(nr, nc, safe)

        for r in range(n):
            if board[r][0] == 'O':
                dfs(r, 0, safe)
            if board[r][m-1] == 'O':
                dfs(r, m-1, safe)
        
        for c in range(m):
            if board[0][c] == 'O':
                dfs(0, c, safe)
            if board[n-1][c] == 'O':
                dfs(n-1, c, safe)

        for r in range(n):
            for c in range(m):
                if board[r][c] == 'O' and (r,c) not in safe:
                    board[r][c] = 'X'

    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])
        dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]

        def check (r, c):
            if r < 0 or r >= n or c < 0 or c >= m or board[r][c] in ['X', '#']:
                return False
            # in bounds, is O-cell, not visited
            return True 

        def dfs(r, c):
            board[r][c] = '#'
            for dx, dy in dirs:
                nr, nc = r + dx, c + dy
                if check(nr, nc):
                    dfs(nr, nc)

        for r in range(n):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][m-1] == 'O':
                dfs(r, m-1)

        for c in range(m):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[n-1][c] == 'O':
                dfs(n-1, c)

        for r in range(n):
            for c in range(m):
                if board[r][c] == 'O':
                    board[r][c] ='X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'