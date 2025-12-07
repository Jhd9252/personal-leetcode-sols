# just use bellmans fords SSSP
# relax all edges |V| - 1 times
# if any edge can be relaxed again
# then there exists a negative cycle
'''

Using Bellman Fords SSSP Relaxation |V| - 1 times
Intution: 
- The shortest path from source to any node is |V| - 1 edges. 
- Any path longer than that is not a shortest path
- If we relax every edge |V| - 1 times, we account for all possible shortest paths. 
- After, if there is an edge that can be relaxed again, there is a negative cycle. 

Input: DAG with non-negative weights (assuming) or negative weights (cycle)
Output: Distance Array 2D

Runtime: O(VE)
Space: O(V+E)
'''

def bellmans(graph: dict, root) -> dict:
    # if required for edge case, get all nodes first, then create
    dist = {node: (float('-inf'), None) for node in graph}
    dist[root] = (0, None)

    n = len(graph)

    # for all edges
    for _ in range(n):
        # for all nodes
        for node in graph:
            # for all edges
            for weight, neighbor in graph[node]:
                # get dist to current node + dist to next node
                possible = dist[node][0] + weight
                # compare distance of next node to recorded
                if possible < dist[neighbor][0]:
                    dist[neighbor] = (possible, node)

    # should have SSSP unless negative weights
    for node in graph:
        for weight, neighbor in graph[node]:
            if dist[node][0] + weight < dist[neighbor][0]:
                raise ValueError('negative cycle')
    return dist 



def rebuild(dist: dict, target) -> list:
    path = []
    while target is not None:
        path.append(target)
        target = dist[target][1]
    return path[::-1]





