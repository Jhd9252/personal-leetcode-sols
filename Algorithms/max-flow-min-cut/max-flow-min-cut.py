'''
Input: Adjacency Matrix

Given: a graph that represents the potential amount of flow going from source to sink


Residual Graph
(1) Where forward edges are potential capcaity left to use
(2) Backward edges are capactities that we want to take back
NOTE: Then forward and backward edges from A->B must be == max flow of that edge

Intuition:
While there exists an augmenting path that can increase flow
Start with zero flow in network
find and update the minimum bottleneck on that path using BFS
update the flow with value, add to maxflow
    - when we add flow from source to sink
    - you decrease flow from sink to source
repeat 
'''

from collections import deque

# algorithm to find the augmenting path if it exists
def bfs(residual_graph, source, sink, parent: dict) -> bool:
    # Find the augmenting path from source to sink (forward edge)
    # Track the parents for the path
    # Return if path exists, modifying out of scope
    # NOTE: Sole purpose, is to find possible paths from source to sink

    visited = set()
    queue = deque([source])
    parent.clear()

    # starting from the source
    while queue:
        node = queue.popleft()
        # explore outgoing edges to find bottleneck
        for cap, nei in enumerate(residual_graph[node]):
            # if we find an unvisited neighbot with unmaxed capacity
            if nei not in visited and cap > 0:
                # then add to visited
                visited.add(nei)
                # set the parent for path, for possible aug
                parent[nei] = node
                # if we ever reach the sink in BFS fashion, we have an augmented path
                if nei == sink:
                    return True
                # add the neighbor onto the potential paths
                queue.append(nei)
    # otherwise, there are no more neigbors unexpllored with cap
    # or we never reached the sink
    return False 

def FFMF(graph, source, sink):
    n = len(graph)
    residual = [row[:] for row in graph] # creates new copies
    maxFlow = 0
    parent = {}

    while bfs(residual, source, sink, parent):
        # find the bottleneck (we can only augment by least)
        # remember, in regular graph, forward edge is max possible flow
        # in residual graph, forward edge is leftover flow, backward edge is used flow
        pathFlow = float('inf')
        v = sink

        while v != source:
            u = parent[v]
            pathFlow = min(pathFlow, residual[u][v])
            v = u 
        
        # update the capacities in both directions
        # NOTE: By finding an augmenting path, we have also guaranteed that the min augmenting amount
        # is available across all edges, thus we update and not check explicitly
        v = sink
        while v != sink:
            u = parent[v]
            residual[u][v] -= pathFlow
            residual[v][u] += pathFlow
            v = u
        
        # update overall flow
        maxFlow += pathFlow

    return maxFlow 


