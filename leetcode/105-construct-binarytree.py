'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Solved
Medium

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary
tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    preorder is [root, left, right]
    in order is [left, root, right]
    We see that preorder gives us the current parent of a local triangle.
    The index that that current parent in inorder array gives us the left and right subtrees.
    Thus, we create a tree from the top down.
    Take the first entry in pre order, create it as a parent node.
    Then set its left and right children / subtrees to be inorder split at its index. 
    It will recurse down until possible children is nothing left, therefore creating NULLs.
    return the current triangle parent upwards as children, until root is returned fully.
    '''


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # for each num in preorder
        # find index in inorder
        # set left child and right child to be arr[:idx] and arr[idx+1:]
        # recurse down, return up the current created node
        root = None
        if inorder:
            root = preorder.pop(0)      # this is current root
            index = inorder.index(root) # get index in inorder [left:right]
            root = TreeNode(root)
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index+1:])
        return root
  
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        Previously, in a balanced tree, our best case is O(nlogn)
        Previosly, in a skewed tree, our worst case is O(n^2)
        Runtime: O(n)
        Space: O(n)
        '''
        inord = {val:idx for idx, val in enumerate(inorder)}
        curr = [0]

        def build(left, right):
            # working with a virtual window (same as index[slice])
            if left > right:
                return None
            val = preorder[curr[0]]
            curr[0] += 1
            root = TreeNode(val)
            index = inord[val]
            root.left = build(left, index-1)
            root.right = build(index+1, right)
            return root
        return build(0, len(inorder)-1)



