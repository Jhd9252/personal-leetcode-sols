'''
199. Binary Tree Right Side View

Medium

Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ''' 
        BFS Level order traversal 
        Runtime: O(n)
        Space: O(n) for queue
        '''
        if not root: return []
        res = []
        q = deque([root])
        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                # root is valid, only add valid children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                # thus, at end of level and is valid
                # append val to res
                if i == qLen - 1:
                    res.append(node.val)
        return res
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        DFS with constant array for result
        Runtime: O(n)
        Space: O(1)
        '''
        res = []
        def dfs(root, level):
            # if we reach the end, do nothing
            if not root:
                return 
            # preprocess: we use post order, visiting right first
            # if our result array == level, then we can add
            # since we visit right first, the first node at next level is rightmost
            # if we backtrack, we already have right most node for level
            if len(res) == level:
                res.append(root.val)
            dfs(root.right, level + 1)
            dfs(root.left, level + 1)

    
        dfs(root, 0)
        return res


        