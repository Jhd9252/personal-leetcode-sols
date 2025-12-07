'''
In an directed graph, a cycle is found if the current working neighbor has already been visited and on stack

'''

def dfs_cycle_directed(graph: dict):
    visited = set()
    stack = set()

    def explore(node):
        # process
        visited.add(node)
        stack.add(node)
        # process neighbors - return True if cycle, else nothing
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if explore(neighbor):
                    return True
            elif neighbor in stack:
                return True
        # down and up, never returned True
        stack.remove(node)
        return False 
