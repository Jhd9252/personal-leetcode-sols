import collections

def kahnsTopologicalSort(edges: list[tuple]):
    
    # not all nodes have outgoing edges -> might not be a key
    nodes = set()

    # create a indegree hashmap
    degree = collections.defaultdict(int)

    # create a graph for ease of use
    graph = collections.defaultdict(list)

    # fill in the graph, indegree and nodes set
    for u, v in edges:
        graph[u].append(v)
        degree[v] += 1
        nodes.add(u)
        nodes.add(v)

    # ensure all nodes in graph
    for node in nodes:
        degree.setdefault(node, 0)
    
    queue = deque([node for node in degree if degree[node] == 0])

    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            degree[neighbor] -= 1
            if degree[neighbor] == 0:
                queue.append(neighbor)
    
    return order if len(order) == len(nodes) else None


    
