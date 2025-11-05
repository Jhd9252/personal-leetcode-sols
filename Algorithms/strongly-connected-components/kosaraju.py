
'''
Given a directed acyclic graph, return its strongly connected components

Kosaraju
1. DFS for finish times stack
2. transpose
3. DFS on reverse finish times


'''

def dfs(graph: dict, node, visited: set, stack: list = None, component: list = None):
    # process
    visited.add(node)

    # part two - component
    if component is not None:
        component.append(node)

    # recurse
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack, component)
    
    # part one - > dfs finish times
    if stack is not None:
        stack.append(node)

def transpose(graph: dict):
    ret = collections.defaultdict(list)
    for node in graph:
        for neighbor in graph[node]:
            ret[neighbor].append(node)
        # if there is no edge to reverse, make sure to include curr
        if node not in ret:
            ret[node] = []
    return ret
        
def kosaraju(graph: dict) -> list:
    # step 1: DFS for finish times
    visited = set()
    stack = []
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited, stack = stack)
    
    # step 2: tranpose
    ret = transpose(graph)

    # step 3: DFS in reverse finish time
    visited = set()
    sccs = []
    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs(ret, node, visited, component = component)
            if component:
                sccs.append(component)
    
    return sccs
