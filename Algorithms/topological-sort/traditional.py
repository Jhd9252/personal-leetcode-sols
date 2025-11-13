def topological_sort(graph: dict):
    # ordering of vertices, using reverse finish times
    # utilizing DFS
    visited = set()
    finish = []

    # recursive DFS
    def dfs(node):
        # base case - add - checks later before recursion
        # pre process (at node, before recursing down)
        visited.add(node)

        # recursion
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        
        # post process (at node, before going up)
        finish.append(node) # array, outside reference, pass by reference

    # call the dfs function starting from source, or for each connected graph component
    for node in graph:
        if node not in visited:
            dfs(node)
    
    return finish[::-1]
