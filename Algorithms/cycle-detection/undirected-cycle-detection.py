


# undirected graph cycle detection

# case 1: neighbor not in visited -> continue
# case 2: neighbor has been visited
#   case 2A: on stack
#       parent? Safe : True
#   case 2B: not on stack
#       safe

def dfs_cycle_undirected(graph: dict):
    visited = set()

    def explore(node, parent):
        # preprocess this node
        visited.add(node)
        # check neighbors -> return True only early
        for neighbor in graph[node]:
            if neighbor not in visited:
                # bubble up True cycles
                if explore(neighbor, node):
                    return True 
            elif neighbor != parent:
                return True
        # return False 
        return False 
    for node in graph:
        if node not in visited:
            if explore(node):
                return True
    return False 




       