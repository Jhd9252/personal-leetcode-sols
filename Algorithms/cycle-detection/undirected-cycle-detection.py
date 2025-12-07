


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
        # process this node
        visited.add(node)

        # check all neighbors
        for neighbor in graph[node]:

            # if the neighbor not visited, explore and bubble up result
            if neighbor not in visited:
                # check if found cycle
                if explore(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        
        # we want to return False for this node only if no cycle in neighbors
        return False 

    for node in graph:
        if node not in visited:
            if explore(node, None):
                return True
    return False 
            
       