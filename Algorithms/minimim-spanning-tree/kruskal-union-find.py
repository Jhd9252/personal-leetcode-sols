#=============================================================
'''
Kruskal Minimum Spanning Tree using Union-Find
RT: O(ElogV)
Space: O(E)


Input: List of edges

Idea: Greedy 
(1) Create a mapping from node <-> ID if needed
(2) create empty edge list, fill it, sort
(3) create a parent hashmap for find
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

    # create variables
    MST = []
    parent = {i: i for i in range(index)}

    # create a mapping from node -> id
    node_index = {}
    index_node = {}
    index = 0
    for node in graph:
        if node not in node_index:
            node_index[node] = index
            index_node[index] = node 
            index += 1

    # create an edge list of outgoing edges using mapping
    edges = []
    for node in graph:
        nodeidx = node_index[node]
        for weight, neighbor in graph[node]:
            neighboridx = node_index[neighbor]
            if (weight, nodeidx, neighboridx) not in edges:
                edges.append((weight, nodeidx, neighboridx))
    # sort the edges, no need for minprio queue
    edges.sort()

    def find(parent: dict, nodeidx):
        # if the current node is not a source of path
        if parent[nodeidx] != nodeidx:
            # compress its path by assigning its parent
            # to be parent in ancestry tree upwards
            parent[nodeidx] = find(parent, parent[nodeidx])
        # once we find it, we return the source parent of path
        return parent[nodeidx]

    def union(parent: dict, A, B):
        # RETURNS: whether a new connection or edge has been made
        # where A, B are node index mappings
        p1 = find(parent, A)
        p2 = find(parent, B)

        if p1 != p2:
            parent[p1] = p2
            return True
    
        return False 
    
    for (weight, nodeidx, neighboridx) in edges:
        if union(parent, nodeidx, neighboridx):
            MST.append((weight, nodeidx, neighboridx))
    
    return MST


# without integer mapping to nodes 
import heapq

def kruskal(graph: dict):
    MST = []
    parent = {}

    # Step 1: Initialize Union-Find parent map
    for node in graph:
        parent[node] = node
        for _, neighbor in graph[node]:
            parent[neighbor] = neighbor  # ensure all nodes are initialized

    # Step 2: Build edge list
    edges = set()
    for node in graph:
        for weight, neighbor in graph[node]:
            # Add edge in canonical order to avoid duplicates (u,v) == (v,u)
            edge = (weight, min(node, neighbor), max(node, neighbor))
            edges.add(edge)

    # Step 3: Sort edges
    sorted_edges = sorted(edges)

    # Step 4: Union-Find functions
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])  # path compression
        return parent[node]

    def union(a, b):
        pa, pb = find(a), find(b)
        if pa != pb:
            parent[pa] = pb
            return True
        return False

    # Step 5: Build MST
    for weight, u, v in sorted_edges:
        if union(u, v):
            MST.append((weight, u, v))

    return MST
