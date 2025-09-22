class Solution:
    '''
    Given mxn matrix with [0,1]
    We have the 1's is land, 0's is water, border is water. 

    BFS or DFS traversal to find adjacent land. Keep a count after all 
    neighbors are exhausted. 
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        ''' BFS approach '''
        n, m = len(grid), len(grid[0])
        count = [0]
        def bfs(r, c):
            queue = deque([(r,c)])
            while queue:
                r, c = queue.popleft()
                # check valid
                if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == '0':
                    continue
                grid[r][c] = '0'
                for (x,y) in [(0,1), (0, -1), (-1, 0), (1, 0)]:
                    nr, nc = x + r, y + c
                    queue.append((nr,nc))
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '1':
                    bfs(r,c)
                    count[0] += 1
        return count[0]

    def numIslands(self, grid: List[List[str]]) -> int:
        ''' DFS approach '''
        n, m = len(grid), len(grid[0])
        count, visited = [0], set()
        def dfs(r, c):
            # check cell valid (pos, water)
            if r < 0 or r >=n or c < 0 or c >= m or grid[r][c] == '0':
                return
            # mark current cell and recurse
            grid[r][c] = '0'
            for (x,y) in [(0,1), (0, -1), (-1, 0), (1, 0)]:
                nr, nc = x + r, y + c
                dfs(nr, nc)
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '1':
                    dfs(r,c)
                    count[0] += 1
        return count[0]
