


import collections

def kahns(edges: list[tuple]):
    nodes = set()
    degree = collections.defaultdict(int)
    graph = collections.defaultdict(list)

    for u, v in edges:
        nodes.append(u)
        nodes.append(v)
        degree[v] += 1
        graph[u].append(v)

    for node in nodes:
        degree.setdefault(node, 0)

    q = deque([node for node in degree if degree[node] == 0])
    
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for neighbor in graph[node]:
            degree[neighbor] -= 1
            if degree[neighbor] == 0:
                q.append(neighbor)

    return order if len(order) == len(nodes) else None

