

def tarjans(graph: dict):
    discover = 0
    index = {}
    lowlink = {}

    stack = []
    on_stack = set()

    sccs = []

    def dfs(node):
        # process this node
        nonlocal discover
        index[node] = discover
        lowlink[node] = discover
        stack.append(node)
        on_stack.add(node)

        # case 1: neighbor not visited -> dfs
        # case 2: neighbor visited, on stack -> in processing -> grab original
        # case 3: neighbor already visited, not on stack -> ignore
        for neighbor in graph[node]:

            # case 1: if neighbor not visited
            if neighbor not in index:
                dfs(neighbor)
                lowlink[node] = min(lowlink[node], lowlink[neighbor])

            # case 2: neighbor visited, on stack, processing, grab original
            elif neighbor in on_stack:
                lowlink[node] = min(lowlink[node], index[neighbor])

            # case 3: neighbor visited, not on stack, done, ignore
        
        # post proccessing -> check if discover == lowlink of this node
        # if it is, then it is a source of SCC of all nodes above on stack
        if lowlink[node] == index[node]:
            component = []
            while True:
                tmp = stack.pop()
                on_stack.remove(tmp)
                component.append(tmp)
                if tmp == node:
                    break
            sccs.append(component)
        
    for node in graph:
        if node not in index:
            dfs(node)
    
    return sccs