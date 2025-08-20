'''
226. Invert Binary Tree

Easy

Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Given a binary tree, not necessarily a BST. 
    Invert the tree, and return its root. 

    Num nodes is [0, 100] inclusive. 

    '''
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        BFS Iterative
        '''
        dummy = root 
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if not node:
                return node 
            node.left, node.right = node.right, node.left 
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return dummy 
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ''' DFS Recursive '''

        def dfs(node):
            # base case 
            if not node:
                return node 
            
            # recursive
            # preprocess 
            node.left, node.right = dfs(node.right), dfs(node.left)

            return node 
        
        return dfs(root)
        
