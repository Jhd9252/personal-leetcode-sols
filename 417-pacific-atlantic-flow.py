class Solution:
    '''
    Water can flow from cell >= cell
    Return a 2d matrix where each list[list[int]] are cells allow
    rain water to flow to both oceans. 

    M1. Call BFS per cell and return [bool(pacific), bool(atlantic)]
    M2. Call DFS per cell and return [bool(pacific), bool(atlantic)]
    M3. Since there are two goals, separate into two sets. 
        - Starting from each ocean set
        - All cells reachable from a border cell, are those that can reach this ocean
        - After both sides, get the intersection. 
    '''
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        p, a = set(), set() 
        dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]
        def dfs(r, c, visited):
            # this node is valided, process
            visited.add((r,c))
            # for each direction
            for (rr, cc) in dirs:
                nr, nc = r + rr, c + cc
                # validate bounds, not explored, < neighbor
                if  (0<=nr<n and 0<=nc<m and 
                    (nr,nc) not in visited and 
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)

        for r in range(n):
            dfs(r, 0, p)
            dfs(r, m-1, a)

        for c in range(m):
            dfs(0, c, p)
            dfs(n-1, c, a)
        return list(p.intersection(a))
        
    

        



        