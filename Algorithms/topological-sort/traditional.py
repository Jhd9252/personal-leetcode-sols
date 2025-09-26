def topological_sort(graph: dict):
    visited = set()
    finish = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        finish.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

            
    return finish[::-1]