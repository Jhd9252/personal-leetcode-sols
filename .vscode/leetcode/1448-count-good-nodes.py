'''
1448. Count Good Nodes in Binary Tree

Medium

Given a binary tree root, a node X in the tree is named good if in the path
 from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Input: root = [3,1,4,3,null,1,5]
Output: 4

Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    A node is labeled good, the node is >= all other nodes on path to node. 
    A root is good. 
    '''
    def goodNodes(self, root: TreeNode) -> int:
        '''
        BFS (Queue with (node, pathMax))
        RT: O(n)
        Space: O(n)
        '''
    def goodNodes(self, root: TreeNode) -> int:
        '''
        DFS (Logic in preprocess)
        Runtime: O(n)
        Space: O(n)
        '''
        res = [0]
        def dfs(node, currMax):
            # base case (end)
            if not node:
                return 

            # preprocess (current) -> determine if good node here, add count
            if node.val >= currMax:
                res[0] += 1
                currMax = max(currMax, node.val)
            # recurse (going down) -> go down with max currently on path
            dfs(node.left, currMax)
            dfs(node.right, currMax)
            # post process (current) nothing

            # return (going up -> post process) nothing
            return
        dfs(root, root.val)
        return res[0]
        