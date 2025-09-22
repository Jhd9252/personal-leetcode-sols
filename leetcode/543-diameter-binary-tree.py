# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        DFS: Recurse until base case. Return 1 + max. Compare split, return on split. 
        RT: O(V+E)
        Space: O(1) 
        '''
        maxDia = [0]
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            maxDia[0] = max(maxDia[0], left + right)
            return 1 + max(left, right)
        dfs(root)
        return maxDia[0]

            
        