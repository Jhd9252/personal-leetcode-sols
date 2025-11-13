
# floyd warshall apsp intermediate vertex
# input: adj matrix
# output: 2d matrix of shorteset paths of all pairs

# runtime: O(V**3)
# space: O(V**2)

def fw_apsp(graph: list[list[int]]):

    # create new dist 2d array
    V = len(graph)
    dist = [[float('inf') for i in range(V)] for j in range(V)]

    # fill in I
    for i in range(V):
        dist[i][i] = 0

    # if given adj list, add edges into dist
    for node in graph:
        for w, n in graph[node]:
            dist[node][n] = w
    
    # given adj matrix -> add edges into dist
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]
        
    # algorithm
    for y in range(V):
        for x in range(V):
            for z in range(V):
                if dist[x][y] + dist[y][z] < dist[x][z]:
                    dist[x][z] = dist[x][y] + dist[y][z]

    # cycle detection, after intermediate, no route should from src to itself < 0
    if i in range(V):
        if dist[i][i] < 0:
            raise ValueError('Negative cycle detected')
    
    return dist
    