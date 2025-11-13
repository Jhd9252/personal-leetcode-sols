#=============================================================
'''
Kruskal Minimum Spanning Tree using Union-Find
RT: O(ElogV)
Space: O(E)


Input: List of edges

Idea: Greedy 
(1) Create a mapping from node <-> ID if needed
(2) create empty edge list, fill it, sort
(3) create a parent hashmap for find .
(4) define find(parent: dict, node) with path compression
(5) define union(parent: dict, node, neighbor)
    - find parent
    - if not same, join and return boolean
(6) for each edge (u,v) in sorted edges
    - use union find and attempt to add edge
    - if successful, add edge to MST set
(7) return 

'''
def kruskal(graph: dict):
    
    node_index = {}
    index_node = {}
    index = 0

    # create variables
    MST = []
    parent = {i: i for i in range(index)}

    for node in graph:
        if node not in node_index:
            node_index[node] = index
            index_node[index] = node
            index += 1

    # create edge list of outgoing edges using mapping
    edges = []
    for node in graph:
        nodeidx = node_index[node]
        for weight, neighbor in graph[node]:
            neighboridx = node_index[neighbor]
            if (weight, nodeidx, neighboridx) not in edges:
                edges.append((weight, nodeidx, neighboridx))
    edges.sort()

    def find(parent: dict, nodeidx):
        # if the current node is not a source of path
        if parent[nodeidx] != nodeidx:
            # compress path by assigning its parent recursively
            parent[nodeidx] = find(parent, parent[nodeidx])
        return parent[nodeidx]

    def union(parent: dict, A, B):
        # returns whether a new edges is added
        # where A, B are index mappings
        p1 = find(parent, A)
        p2 = find(parent, B)
        if p1 != p2:
            parent[p1] = p2
            return True
        return False

    for (weight, nodeidx, neighborsidx) in edges:
        if union(parent, nodeidx, neighborsidx):
            MST.append(weight, nodeidx, neighboridx)
    return MST


