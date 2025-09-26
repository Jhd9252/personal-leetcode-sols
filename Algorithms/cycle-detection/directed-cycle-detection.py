'''
In an directed graph, a cycle is found if the current working neighbor has already been visited and on stack

'''

def dfs_cycle_directed(graph: dict):
    visited = set()
    stack = set()

    def explore(node):
        # pre process
        visited.add(node)
        stack.add(node)
        # process and bubble up True cycle found
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if explore(neighbor):
                    return True
            elif neighbor in stack:
                return True
        # post process - remove from stack, return False 
        stack.remove(node)
        return False 

    for node in graph:
        if node not in visited:
            if explore(node):
                return True
    return False 
    

    