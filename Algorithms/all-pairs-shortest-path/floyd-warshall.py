# Floyd Warshall APSP: Intermediate Vertex

# - Input: Adjacency MAtrix with weights
# - Output: 2D matrix of shortest paths distance of all pairs
# - Idea: treat each node as an intermediate node between all other pairs
# - I.E, if the path between x->y + y->z is shorter than x->z, then update

# - runtime: O(V**3)
# - space: O(v**2)


def floyd_warshall(graph: list[list[int]]):

    # create a new distance 2D array
    V = len(graph)
    dist = [[float('inf') for i in range(V)] for j in range(V)]

    # fill in the ii
    for i in range(V):
        dist[i][i] = 0

    # if given adj list, add edges into dist
    for node in graph:
        for weight, neighbor in graph[node]:
            dist[node][neighbor] = weight 

    # if given adj martix-> add edges to dist
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]

    # algorithm
    for y in range(V):
        for x in range(V):
            for z in range(V):
                if dist[x][y] + dist[y][z] < dist[x][z]:
                    dist[x][z] = dist[x][y] + dist[y][z]
    

    # detect cycles -> after intermediate vertex, no route should be less than node to itself == 0
    for i in range(V):
        if dist[i][i] < 0:
            raise ValueError('Negative cycle')
        
    return dist 

    