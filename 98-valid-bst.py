'''
98. Validate Binary Search Tree

Medium

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Binary Search Tree if 
    left <= node <= right
    left and right subtrees are also BST
    The left subtree must contain only keys < node
    the right subtree must contain only keys > node.
    This is easy if viewing from the current level : left.val < node.val < right.val
    But expanding our view to the max(left) < node.val < min(right) is the challenge. 

    '''
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        DFS with nonlocal min and max values
        When we move left, we update the maximum to be parent
        When we move right, we update the minimum to be parent 
        Runtime: O(n)
        Space: O(n)
        '''
        INF = sys.maxsize
        def dfs(node, lower, upper):
            # base case: node DNE, then valid BST
            if not node:
                return True
            
            # node is valid: check current view
            if lower < node.val < upper:
                return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)
            # else node is not BST valid
            return False 
        
        return dfs(root, -INF, INF)

    
        