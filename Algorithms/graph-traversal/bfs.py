import collections

def bfs(graph: dict, root):
    if not graph or not root: return []
    res = []
    visited = set()
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        visited.add(node)
        res.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    
    return res

