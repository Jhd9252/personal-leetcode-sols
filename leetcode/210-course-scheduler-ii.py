class Solution:
    '''
    Abstract: Graph problem, asking if we can return an ordering to finish courses.
    Part 1: Determine if no cycle AND can finish courses
    Part 2: Return an ordering of courses. 
    '''
    def build(self, edges, numCourses):
        adjlist = {}
        for v in range(numCourses):
            adjlist[v] = []
        for b, a in edges:
            adjlist[a].append(b)
        return adjlist

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ''' DFS (to find cycle AND return reverse finish times)'''
        visited, stack, finish = set(), [], []
        graph = self.build(prerequisites, numCourses)
        def dfs(node):
            if node in visited:
                if node in stack:
                    return True
                return False 

            visited.add(node)
            stack.append(node)

            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True 
            
            finish.append(node)
            stack.pop()
            return False 

        for node in graph:
            if dfs(node):
                return []
        return finish[::-1]

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ''' Kahns Indegree Topological Sort '''
        graph = self.build(prerequisites, numCourses)
        indegree = collections.defaultdict(int)
        res = []
        queue = deque([])

        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        
        for node in graph:
            if indegree[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            res.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return res if len(res) == numCourses else []

        