'''
572. Subtree of Another Tree

Easy

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, curr, test):
        ''' 
        Check current node is starting point -> Continue 
        RT: O(m) where m is number of nodes in subroot
        Space: O(H) where H is height of subtree
        '''

        # if both nodes DNE-> return True 
        if not curr and not test:
            return True

        # if both nodes Exist and are equal, recurse further
        if curr and test and curr.val == test.val:

            # return if left and right subtrees rooted HERE are equal
            return self.check(curr.left, test.left) and self.check(curr.right, test.right)

        # If only one exists -> return False 
        return False


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        Check root is anchor, if not, recursively call on left and right
        Runtime: O(n * m) where n=nodes in root, m=nodes in subtree
        Space: O(H) where H is height of root
        '''

        # Base case: if subroot is empty tree, then return True
        if not subRoot:
            return True

        # base case: subroot exists, but root does not, return False 
        if not root: 
            return False

        # if both nodes exist, if anchor and same, return True
        if self.check(root, subRoot):
            return True

        # else both nodes exist, not anchor
        # check left and right substrings
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    ########################################################################################

    def isSubTree(self, root, subRoot):
        ''' 
        KPM Algorithm
        (1) Convert each subtree in some order. 
        (2) Use KPM to search in post processing. 
        RT: Convert + LPS + KMP = O(n) + O(m) + O(n+m) = O(n+m)
        Space: Convert + LPS = O(n) + O(m) = O(n+m)
        '''
        return self.KMP(self.convert(root), self.convert(subRoot))
    
    def convert(self, node):
        ''' 
        RT: O(n)
        Space: O(n)
        '''
        # base case:
        if not node:
            return "#"
        return "^" + str(node.val) + self.convert(node.left) + self.convert(node.right) + "#"

    def LPS(self, substring):
        m = len(substring)
        lps = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and s[i] != s[j]:
                j = lps[j-1]
            if s[i] == s[j]:
                j += 1
                lps[i] = j
        return lps

    def KPM(self, string, substring):
        lps = self.LPS(substring)
        n = len(string)
        m = len(substring)
        j = 0
        for i in range(n):
            while string[i] != substring[j] and j>0:
                j = lps[j-1]
            if string[i] == substring[j]:
                j += 1
                if j == m:
                    return True
        return False 

  
    
    
        