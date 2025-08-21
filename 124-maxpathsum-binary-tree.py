# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Path in Binary Tree: Sequence of nodes where each pair is adjacent with an edge. 
    A node can only appear once. Path does not require root. 
    Path Sum in Binary Tree: Sum of nodes' values in the path. 
    Given the root of a binary tree, return the maximum path sum of any non-empty path. 

    Since path does not require root node of entire binary tree, 
    we need to observe all possible paths that also exclude the root. 
    If we iterate through each node, and consider all possible paths that pass through 
    this node from left and right, we can build up. 
    For instance, we have nodeX with left nodeY and right nodeZ.
    If nodeX + nodeY > nodeX + nodeZ, then we pass the sum of nodeX+nodeY upwards. 
    At each node, we compare two things
    (1) What is that maxpath sum rooted at current node: left + right + node
    (2) What is the nonsplit path we can return upwards for parent comparison
    '''
    def __init__(self):
        self.sum = float('-inf')
    
    def maxPathSum(self, root) -> int:
        self.dfs(root)
        return self.sum

    def dfs(self, node):
        if not node: return 0

        left = max(0, self.dfs(node.left))
        right = max(0, self.dfs(node.right))

        # split comparison: as if maxpathsum is rooted here
        self.sum = max(self.sum, left + right + node.val)

        # non-split comparison, pass the longest to parent
        return max(left, right) + node.val

    def maxPathSum(self, root) -> int:
        res = [float('-inf')]
        def dfs(root):
            if not root: return 0
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            res[0] = max(res[0], root.val + left + right)
            return root.val + max(left, right)
        dfs(root)
        return res[0]
