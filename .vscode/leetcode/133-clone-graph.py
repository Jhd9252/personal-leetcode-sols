"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

Clone a graph:
Use DFS/BFS to traverse the graph
Use a hashmap to track already visited nodes, and cloned nodes. 

Push each node onto a queue, make sure the node is already cloned. 
Process neighbors. 
If neighbor is already cloned and visited, append to current clone's neighbor. 
Otherwise, clone the neighbor, append to queue. 
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node

        cloneMapper = {node.val: Node(node.val, [])} # {real : new clone}
        queue = deque([node]) # add all nodes to queue

        while queue:
            curr = queue.popleft()
            clone = cloneMapper[curr.val] # grab the cloned node
            
            for neighbor in curr.neighbors:
                # check if neighbor is cloned as well (in case no incoming edges)
                if neighbor.val not in cloneMapper:
                    cloneMapper[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                # in any case, append this neighbor to current neighbor
                clone.neighbors.append(cloneMapper[neighbor.val])
        
        return cloneMapper[node.val]



        
        