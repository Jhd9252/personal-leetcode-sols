class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # if not mat or mat[0]: return []
        
        for col in range(len(mat[0])):
            cells = []
            values = []
            r,c = 0, col
            while r < len(mat) and c < len(mat[0]):
                cells.append((r,c))
                values.append(mat[r][c])
                r += 1
                c += 1
            values.sort()
            for (x, y) in cells:
                mat[x][y] = values.pop(0)
        
        for row in range(len(mat)):
            cells = []
            values = []
            r, c = row, 0
            while r < len(mat) and c < len(mat[0]):
                cells.append((r,c))
                values.append(mat[r][c])
                r += 1
                c += 1
            values.sort()
            for (x,y) in cells:
                mat[x][y] = values.pop(0)
        return mat

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        NOTE: each diaongal has a slope of -1
        NOTE: difference in row-col is unique, in a grid ranges from [-,+]  
        Create a hashmap from {i-j: [values of [i][j]]}   
        Can use sort() for nlogn or heappush for logn
        Iterate through each cell again, set the values
        '''
        n, m = len(mat), len(mat[0])
        d = collections.defaultdict(list)
        for i in range(n):
            for j in range(m):
                heapq.heappush(d[i-j], mat[i][j])

        for i in range(n):
            for j in range(m):
                mat[i][j] = heapq.heappop(d[i-j])

        return mat  
