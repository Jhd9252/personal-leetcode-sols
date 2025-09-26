
'''
Prim's Algorithm for Minimum Spanning Tree
Attributes: BFS, Minimim Priority Queue for lowest cost edge that is connected, greedy

Input: adjlist list {node: [(weight, neighbor)]}

Intuition: 
1. start with an empty visited set, edge list, root
2. start with (0, root, None/parent), find the safe outgoing edge
3. add that edge to our set
4. add all outgoing edges from destingation node taht is unvisited to q
5. repeat

this works because, the cut theorem states that the lowest cost edge from one set to another always exists in every MST

Proof by contradition:
Let S be working MST
Let T be a full MST
Let V be the vertex set

Say that the lowest cost edge from S to V-S, is (u, v). 
Let's assume then, that the cut theorem is false. 
Then if T is a full MST, then at some point, there must exist a smaller than edge from S to V-S, that exists in MST T. 
Say that edge is (x,y).

Then (x,y) must be strictly less than (u,v). 
But, since (u,v) is stated to be the minimum cut, then (x,y) !< (u,v). 
And therefore T is not a full MST. 

Runtime: O(ElogV)
Space: O(V)

Why this runtime:

we are pushing at most O(V) times, taking O(logV) each time
we are popping at most O(E) times, taking at most O(logV) each time
MST size is bounded by |V|-1


'''
import heapq

def prims(graph: dict, root, visited: set = None):

    # create MST
    MST = []

    # create visited set, node is visited if it has been added
    visited = visited if visited else set()

    # holds the outgoing edges of visited nodes (nodes in forest)
    # in sorted order 
    minHeap = [(0, root, None)]

    while minHeap:
        
        # By CUT THEOREM, this is the lowest cost edge from {S} -> {V-S}
        cost, node, parent = heapq.heappop(minHeap)

        # This checks if node already in MST to avoid duplicate edges 
        # Because we add a node to visited only if we added a cut edge, which is guaranteed. 
        if node in visited:
            continue

        # At this point, we have the cut edge, so we add node to visited
        visited.add(node)

        # greedily add this edge to MST  
        if parent is not None:
            MST.append((parent, node, cost))

        # Explore every out going edge from this node 
        for weight, neighbor in graph[node]:

            # if a node has been explored already, cut theorem states we already found that cut edge, skip
            # Skipping here allows some optimization to avoid pushing unnecessary edges, cleaner 

            # If not visited, we haven't found a cut edge connecting outside MST to neighbor, add to heap
            if neighbor not in visited:
                heapq.heappush(minHeap, (weight, neighbor, node))
    
    # invariant is that MST only has cut edges 
    # our condition is that only not visited nodes are pushed to minHeap
    # each loop, we add a cut edge, or skip duplicate edges
    # thus, at termination, when minHeap is empty or all nodes are visited, MST is valid. 
    return MST


def prims_forest(graph: dict):
    forest = []
    visited = set()

    for node in graph:
        if node not in visited:
            mst = prims(graph, node, visited)
            if mst:
                forest.append(mst)
            # if want flat 
            # flat_forest.extend(mst)
    return forest

# assumes mst_edges is a flat forest of edges
def total_weight(mst_edges):
    return sum(weight for _, _, weight in mst_edges)
