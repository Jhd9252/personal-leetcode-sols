class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r, c):
            # base case: return area 0
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == 0:
                return 0
        
            # process this cell
            grid[r][c] = 0
            total = 1
            # recurse
            for (x,y) in [(0,1), (0, -1), (1,0), (-1, 0)]:
                nr, nc = r + x, c + y
                total += dfs(nr, nc)
            # return total up to previous postprocess
            return total 
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ''' BFS Approach '''
        n, m = len(grid), len(grid[0])
        maxArea = 0

        def bfs(r, c):
            ''' BFS returns count of cells going through queue that are valid '''
            queue = deque([(r,c)])
            count = 0
            while queue:
                r, c = queue.popleft()
                if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == 0:
                    continue
                count += 1
                grid[r][c] = 0
                for (x,y) in [(0,1), (0, -1), (1,0), (-1, 0)]:
                    nr, nc = r + x, c + y
                    queue.append((nr,nc))
            return count
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    maxArea = max(maxArea, bfs(i,j))
        return maxArea



            

        