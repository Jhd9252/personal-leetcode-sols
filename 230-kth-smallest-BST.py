# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            if node:
                return dfs(node.left) + [node.val] + dfs(node.right)
            else:
                return []
        return dfs(root)[k-1]

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            if not node: return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        res = []
        dfs(root)
        return res[k-1]


            