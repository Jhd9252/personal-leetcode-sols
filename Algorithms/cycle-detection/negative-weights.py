# just use bellmans fords SSSP
# relax all edges |V| - 1 times
# if any edge can be relaxed again
# then there exists a negative cycle

'''
Bellman Fords: Single Source shortest path

Intuition: 
- The shortest path from source to any node is at most |V| - 1 edges.
- Any path longer than that is not a shortest path
- Thus, if we relax every single edge |V| -1 times, we can account for all possible shortest paths
- After, if there is an edge that CAN be relaxed again, there exists a negative cycle. 

Input: DAG with non-negative or negative weights 
Output: Distance Hashmap

Runtime: O(VE)

Space: O(V + E)
'''

def bellman_ford(graph: dict, root) -> dict:
    dist = {node: (float('-inf'), None) for node in graph}
    dist[root] = (0, None)

    n = len(graph)

    # for |V| - 1 times 
    for _ in range(n):
        
        # iterate through all nodes
        for node in graph:
            # iterate through all edges
            for weight, neighbor in graph[node]:
                
                # get the dist to this node + distance to neighbor
                possible = dist[node][0] + weight
                
                # if dist_to_this_node + dist_neighbor < recorded_dist_neighbor
                # relax
                if possible < dist[neighbor][0]:
                    dist[neighbor] = (possible, node)

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




