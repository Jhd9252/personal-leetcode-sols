'''
Given a 2d matrix of integers, flood fill a certain color in cardinal directions
Given multiple starting points

DFS approach
'''
def floodfill(matrix: list[list[int]]):
    # exceptions
    if not matrix or not matrix[0]: return matrix

    # obtain directions
    ROWS = len(matrix)
    COLS = len(matrix[0])

    # colors
    OLD_COLOR, NEW_COLOR = matrix[0][0], matrix[0][1] # first cell, (first_row, second col)

    # as we traverse, skip repeated calls
    visited = set()

    # DIRS
    dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def dfs(r, c):
        # given a cell, check if its valid and needs to be changed
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or matrix[r][c] != OLD_COLOR or (r,c) in visited:
            return 
        
        # process
        matrix[r][c] = NEW_COLOR
        visited.add((r,c))

        # recursion travel
        for dx, dy in dirs:
            nr = r + dx
            nc = c + dy
            dfs(nr, nc)
        
    for r in matrix:
        for c in matrix[r]:
            if (r,c) not in visited:
                dfs(r,c)


# single start point
def flood_fill(matrix, start_row, start_col, new_color):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    OLD_COLOR = matrix[start_row][start_col]
    visited = set()

    def is_valid(r,c):
        return 0 <= r < len(matrix) and 0<=c<len(matrix[0]) and matrix[r][c] == OLD_COLOR and ((r,c) not in visited)

    def dfs(r,c):
        if is_valid(r,c):
            visited.add((r,c))
            matrix[r][c] = NEW_COLOR
            for dr, dc in dirs:
                dfs(r+dr, c+dc)
        
    # call DFS on starting point 
    dfs(start_row, start_col)