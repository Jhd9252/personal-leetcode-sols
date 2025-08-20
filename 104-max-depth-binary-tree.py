# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ''' BFS Level Count '''
        if not root: return 0
        depth = 1
        queue = deque([(root, 1)])

        while queue:
            qLen = len(queue)
            for i in range(qLen):
                node, level = queue.popleft()
                depth = max(depth, level)
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
        return depth
    
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ''' DFS return count upwards '''
        
        def dfs(node):
            # base case
            if not node:
                return 0
            # recurse, post process + 1, return upwards
            return 1 + (max(dfs(node.left), dfs(node.right)))

        return dfs(root)


