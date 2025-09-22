'''
235. Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Solved
Medium

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        Lowest Common Ancestor 
        Conditions:
        If current node is greater than both p and q: Its a common ancestor, move left
        If current node is less than both p and q: Its a common ancestor, move right
        If a node is equal to either, or has them in left and right, its a LCA
        '''
        curr = root
        # ends if curr is NULL
        while curr:
            # if both p and q are less than curr, go left
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left 
            # if both p and q are greater than curr, go right
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # else, we have p<=curr<=q or q<=curr<=p
            # thus lowest common ancestor
            else:
                return curr
        # either curr is LCA, or is None and no LCA found
        return curr
