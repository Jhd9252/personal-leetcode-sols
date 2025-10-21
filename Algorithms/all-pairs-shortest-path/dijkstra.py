
# SSSP (src -> all other nodes)
# Runtime: O((V+E) Log V)
# Space: O(V+E)
# Idea: MinPrio Q for lowest cost edge

# APSP using Dijkstra's
# Runtime: O(V*(V+E)LogV)
# Space: O(V+E) * O(V)
def dijkstra(graph: dict, root) -> dict:
    dist = {node: (float('inf'), None) for node in graph}
    dist[root] = (0, None)

    minPrio = [(0, root)] # heapq minheap -> (dist to node, node)
    while minPrio:
        curr_dist, curr_node = heapq.heappop(minPrio)
        if curr_dist > dist[curr_node]:
            continue
        for weight, neighbor in graph[curr_node]:
            if curr_dist + weight < dist[neighbor]:
                dist[neighbor] = curr_dist + weight
                heapq.heappush(minPrio, (curr_dist + weight, neighbor))
    return dist

def apsp(graph: dict) -> dict:
    apsp = {}
    for node in graph:
        apsp[node] = dijkstra(graph, node)
    return apsp





# dijkstra -> from single soruce we get {node: (dist, parent)}
# apsp -> { source : { node: (dist, parent)}}




    