'''
Dijkstra's Single source shortest path

input: directed or undirected graph with non-negative weights
- if undirecrted graph, double all edges and assign directions

output: distance hashamp { node: (dist, prev))
- if we want to rebuild the path, track (distance, node, prev) and follow backwards

Idea:
1. starting from root, use a min prio queue to get the next lower cost edge from source path
2. update distances when current distance + weight < recorded distance to next node
3. push newly updated weighted node to queue 
4. each cycle, check if already current

Runtime: O((V+E)logV) with Min Prio Queue, Exploring edges is O(ElogV)
- creating dist, minPrio = O(V), O(V)
- Heappop from minprio at most O(V*logV) times
- explore all edges, and push at most O(ELogV) times
- O(VlogV) + O(ELogV) = O((V+E) log V))


Space: O(V+E)
'''
import heapq
def dijkstras(graph: dict, root):

    # track {destination : (dist from source, parent)}
    dist = {node: (float('-inf'), None) for node in graph}
    dist[root] = (0, None)

    # only tracks (currently updated distance, to this node)
    minPrio = [(0, root)] # (dist, node)

    while minPrio:
        # pop the lowest connecting neighbor
        cost, node = heapq.heappop(minPrio)
        
        # check if current < recorded, if it is, skip
        if cost < dist[node]:
            continue

        # valid current dist, check outgoing edges
        for w, n in graph[node]:
            if cost + w < dist[n][0]:
                dist[n] = (cost + w, node)
                heapq.heappush(minPrio, (cost+w, n))
    return dist

def rebuild(dist: dict, target):
    path = []
    while target != None:
        path.append(target)
        target = dist[target][1]
    return path[::-1]



