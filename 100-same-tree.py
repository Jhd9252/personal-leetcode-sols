'''
100. Same Tree

Easy

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    We know that two binary trees are the same if for every node, their subtrees are the same.
    BFS with two queues. 
    Traverse both trees in-order and compare
    DFS on both trees and returning if both subtrees are the same. 
    '''
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            # base case: both are None -> True
            if not p and not q: return True
            # base case: one of them is None -> False
            if not p or not q: return False
            # both exist - is equal
            if p.val == q.val:
                return dfs(p.left, q.left) and dfs(p.right, q.right)
            # both exists - not equal
            return False
        return dfs(p, q)

     
    def isSameTree(self, p, q) -> bool:
        # only continue if both nodes exist
        if p and q:
            # we need to preprocess check both nodes
            # then recurse and compare subtrees
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # otherwise both nodes DNE or one DNE
        # if both nodes DNE -> True
        # if one side DNE -> False
        return p is q
