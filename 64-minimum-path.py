
class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
        ''' Backtrack/DFS with runtime O(2^(m+n)), O(1) Space '''
        # result
        res = [float('inf')]
        # vars
        m, n = len(grid), len(grid[0])

        # consider every possible path of down or right
        def backtrack(grid, r, c, total):
            # base case : invalid bounds
            if r >= m or c >= n:
                return
            # base case: reached the end of a possible path
            if r == m - 1 and c == n - 1:
                # record the possible answer
                res[0] = min(res[0], total + grid[r][c])

            # at this point, consider both the down 
            backtrack(grid, r + 1, c, total + grid[r][c])

            # and the right 
            backtrack(grid, r, c + 1, total + grid[r][c])

        # call the function and return 
        backtrack(grid, 0, 0, 0)

        return min(res)


    def minPathSum(self, grid: List[List[int]]) -> int:
        ''' 
        Dynamic Programming top down memoization 
        - The end cell's answer is the minimum between min((r-1, c), (r, c-1)) + curr
        - The same if true for every cell 
        - Then the base case if beginning, where answer = curr
        - if we reach a boundary, then end the recursion and return infinity
        - memoization to save compute time
        '''

        m, n = len(grid), len(grid[0])
        memo = {} # (r,c) : min(top, left) + current
        def recurse(r, c):
            # base case : bounds
            if r < 0 or c < 0:
                return float('inf')
            # base case: in memo
            if (r, c) in memo: 
                return memo[(r,c)]

            # base case beginning
            if (r, c) == (0,0):
                return grid[r][c]
            
            # post process = recursion
            memo[(r,c)] = min(recurse(r-1, c), recurse(r, c-1)) + grid[r][c]

            # return to higher recursion
            return memo[(r,c)]
        return recurse(m-1, n-1)

    def minPathSum(self, grid: List[List[int]]) -> int:
        ''' BFS '''
        res = [float('inf')]
        def bfs(grid, r, c):
            q = deque([(r, c, 0)])
            visited = set()
            while q:
                r, c, total = q.popleft()

                if r >= len(grid) or c >= len(grid[0]):
                    continue
                if r == len(grid) - 1 and c == len(grid[0]) - 1 and (r, c) not in visited:
                    res[0] = min(res[0], total + grid[r][c])
                    continue
                visited.add((r,c))
                total += grid[r][c]
                q.append((r+1, c, total))
                q.append((r, c+1, total))
        bfs(grid, 0, 0)
        return res[0]

    def minPathSum(self, grid: List[List[int]]) -> int:
        ''' 
        Dynamic Programming Bottom up 
        Starting at the simplest case of cell (0,0), we know the min sum to this spot
        If we can travel only right or down, then the min sum to cell (i,j)
            if the minimum of prev possible cells + current
        the edge cases are if top row, or left col
            if in leftmost column == 0, then grid[i][j] += grid[i-1][j]
            if in topmost row == 0, then grid[i][j] += grid[i][j-1]
        otherwise, there is a left and up, so min(left, up) + current
        '''
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if (i, j) == (0, 0):
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]
                
            
    
        

    
                






    

    



        