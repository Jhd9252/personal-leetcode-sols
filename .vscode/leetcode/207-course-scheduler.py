class Solution:
    '''
    Abstract this into a graph problem
    Given an edge (a, b), the direction is b -> a. 
    We want to find if we can finish all courses
    
    
    M1. DFS directed graph cycle detection (stack)
    Asking if there is not loop that requires a class on our stack. 
    Cycle detection in directed graph dfs, if on stack, return False 

    We could actually use an array for faster lookup instead of a set

    M2. Kahn's algorithm (BFS) Topological Sort 
    If a cycle exists, we won't be able to process all nodes.
    Or if we have nodes with non-zero indegree at the end, there is a cycle.
    If we can process all nodes, return True

    '''
class Solution:

    def buildAdjList(self, preq: list[list[int]]) -> dict:
       
        adjlist = collections.defaultdict(list)
        for (b, a) in preq:
            adjlist[a].append(b)
            if b not in adjlist:
                adjlist[b] = []
        return adjlist

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        ''' DFS cycle detection (on stack / processing) '''
        graph = self.buildAdjList(prerequisites)
        visited = set()
        stack = []
        def dfs(node):
            # base case: if node has been visited
            if node in visited:
                if node in stack:
                    return True
                return False
            
            # otherwise not visited -> not end -> process
            visited.add(node)
            stack.append(node)

            # process neighbors
            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True 
            
            # done post processing
            stack.pop()

            # otherwise, there is no cycle at this node or underneath it 
            return False
        
        # call DFS on every node
        # NOTE: dfs returns TRUE if cycle, question is asking return False if cycle
        for node in graph:
            if dfs(node):
                return False 
        return True 
        
    def canFinish(self, n, prerequisites):
        ''' Topological Sort with BFS '''
        G = [[] for i in range(n)]
        degree = [0] * n
        for j, i in prerequisites:
            G[i].append(j)
            degree[j] += 1
        bfs = [i for i in range(n) if degree[i] == 0]
        for i in bfs:
            for j in G[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return len(bfs) == n

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ''' DFS wtih a single array for [unvisited = 0 , processing = -1, done processing = 1] '''

        state = [0] * numCourses

        def dfs(val):
            if state[val] == 1:
                return False 
            if state[val] == -1:
                return True 
            state[val] = -1 

            for i in graph[val]:
                if dfs(i):
                    return True
            state[va] = 1
            return False 
        for v in range(numCourses):
            if dfs(v):
                return False
        return True
