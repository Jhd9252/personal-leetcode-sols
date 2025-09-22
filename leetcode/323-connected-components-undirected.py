class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1] * n

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> bool:
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return False

            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

            return True

        components = n
        for u, v in edges:
            if union(u, v):
                components -= 1

        return components
    
def countComponents(self, n: int, edges: List[List[int]]) -> int:
    ''' Use DFS to create components and increment per tree found '''
    def build_graph(n: int, edges: List[List[int]]) -> Dict[int, List[int]]:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph
    
    def dfs(node: int) -> None:
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    graph = build_graph(n, edges)
    visited = set()
    components = 0
    for i in range(n):
        if i not in visited:
            dfs(i)
            components += 1
    return components 