class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        # exceptions
        if not grid or not grid[0]: return -1 

        # track fresh oranges and minutes
        minutes = 0
        fresh = 0

        # need a queue to track all orotten oranges
        queue = deque([])

        # for each cell, add to queue or fresh count
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        # Operate only if there are fresh oranges and unprocessed rotten oranges
        while queue and fresh > 0:
            minutes += 1

            # process rotten oranges on this current level (minute)
            qLen = len(queue)
            for _ in range(qLen):
                x, y = queue.popleft()

                # visit neighbors
                for dx, dy in [(0,1), (0, -1), (1,0), (-1, 0)]:
                    xx, yy = x + dx, y + dy
                    # validate bounds
                    if xx < 0 or xx>=n or yy < 0 or yy >= m:
                        continue
                    # validate value
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                    # otherwise, fresh orange -> update
                    fresh -= 1
                    grid[xx][yy] = 2
                    queue.append((xx,yy))
        
        # check if minutes and fresh
        return minutes if fresh == 0 else -1

        
