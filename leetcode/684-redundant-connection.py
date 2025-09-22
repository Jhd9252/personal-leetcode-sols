class Solution:
    '''
    A tree is an undirected and connected graph with no cycles. 

    We have nodes [1,n] with one additional edge added. 
    The graph is a array of edges of length n where edges[i] = [a, b] where A-> B. 
    Return an edge that can be removed so that the resulting graph is a tree of n nodes only. There are multiple answeres. 
    Return the answer that occurs last in input. 

    Minimum spanning tree problem 
    PrimsMST is for connected directed with adjlist
    Kruskal is for Union find with edge list
    '''
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        res = []

        def find(parent: dict, node):
            if parent[node] != node:
                parent[node] = find(parent, parent[node])
            return parent[node]

        def union(parent: dict, A, B):
            rootX = find(parent, A)
            rootY = find(parent, B)
            if rootX != rootY:
                parent[rootX] = parent[rootY]
                return True 
            return False 

        # create a parent list 
        parent = {i: i for i in range(1, len(edges) + 1)}

        for A, B in edges:
            if not union(parent, A,B):
                res.append([A,B])
        return res[-1]


        
        