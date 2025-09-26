

def dfs(graph: dict, visited, root):
    # base case, return empty 
    if not graph or not visited or not root: return []

    # preprocess, creates a result for this node
    res = [root]

    # traverse down
    for neighbor in graph[node]:
        if neighbor not in visited:
            # take the lower result and append this level 
            res += dfs(graph, visited, neighbor)
            
    # return this level up into the assignment 
    return res 

