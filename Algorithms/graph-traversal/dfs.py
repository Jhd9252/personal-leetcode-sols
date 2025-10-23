

# DFS works as (white: undiscovered, grey: current, black: discovered)
# DFS can be iterable with a stack OR recursive


# iterative with stack (goes right to left unless swap)
def dfs(graph: dict, visited, root):
    if not graph or not visited or not root: return []
    res = [root]
    stack =[root]
    while stack:
        node = stack.pop()
        if node:
            res.append(node)
            stack.append(node.left)
            stack.append(node.right)
    


# recursive on each component source of a single graph, without assumption of connected
def dfs(graph: dict, visited, root):

    # exceptions, base
    if not graph or not visited or not root: return []

    # preprocessing (before going down): capture this node 
    res = [root]

    # process (recurse)
    for neighbor in graph[root]:
        if neighbor not in visited:
            res.append(dfs(graph, visited, neighbor))

    # post process (after going down, what are we returning up): return res to append upper
    return res

