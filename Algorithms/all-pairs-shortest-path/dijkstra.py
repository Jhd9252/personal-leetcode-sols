# Use dijkstra SSSP for every single node
    
# Dijkstras 
# - runtime: O((V+E) log V)
# - Space: O(V+E)

# APSP using Dijkstras
# - runtime: O(V * (V+E)logV)
# - space: 




def dijkstra(graph: dict, root):
    dist = {node: (float('inf'), None) for node in graph}
    dist[root] = (0, None)

    minPrio = [(0, root)]

    while minPrio:
        curr_dist, curr_node = heapq.heappop(minPrio)
        if curr_dist < dist[curr_node]:
            continue
        for weight, neighbor in graph[curr_node]:
            if curr_dist + weight < dist[neighbor]:
                dist[neighbor] = curr_dist + weight
                heapq.heappush(minPrio, (curr_dist + weight, neighbor))
    
    return dist 

def apsp(graph: dict):
    apsp = {}
    for node in graph:
        apsp[node] = dijkstra(graph, node)
    return apsp

# dijkstra -> from single soruce we get {node: (dist, parent)}
# apsp -> { source : { node: (dist, parent)}}




    