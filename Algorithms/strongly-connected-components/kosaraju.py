
'''
Given a directed acyclic graph, return its strongly connected components

Kosaraju
1. DFS for finish times stack
2. transpose
3. DFS on reverse finish times


'''

def dfs(graph: dict, node, visited: set, stack: list = None, component: list = None):

    # process here
    visited.add(node)

    # if second DFS -> component process
    if component is not None: 
        component.append(node)

    # recurse
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack, component)
    
    # post process -> finish times
    if stack is not None:
        stack.append(node)


def transpose(graph: dict):
    transposed = collections.defaultdict(list)
    for node in graph:
        for neighbor in graph[node]:
            transposed[neighbor].append(node)
        # node might have zero outgoing edges, so wont be in transposed
        if node not in transposed:
            transposed[node] = []
    return transposed


def kosaraju(graph: dict) -> list:

    # step 1: DFS for finish times
    visited = set()
    stack = []
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited, stack = stack)
    
    # step 2: transpose
    transposed = transpose(graph)

    # step 3: DFS in reverse finish times
    visited = set()
    sccs = []
    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs(transposed, node, visited, component = component)
            if component:
                sccs.append(component)
    return sccs
