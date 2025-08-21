# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        # use level order traversal to match LeetCode's serialization format
        flat_bt = []
        queue = collections.deque([root])
        while queue:
            node = queue.pop()
            if node:
                flat_bt.append(str(node.val))
                queue.appendleft(node.left)
                queue.appendleft(node.right)
            else:
                # you can use any char to represent null
                # empty string means test for a non-null node is simply: flat_bt[i]
                flat_bt.append('')
        return ','.join(flat_bt)
    # time:  O(n)
    # space: O(n)

    def deserialize(self, data):
        if not data:
            return
        flat_bt = data.split(',')
        ans = TreeNode(flat_bt[0])
        queue = collections.deque([ans])
        i = 1
        # when you pop a node, its children will be at i and i+1
        while queue:
            node = queue.pop()
            if i < len(flat_bt) and flat_bt[i]:
                node.left = TreeNode(int(flat_bt[i]))
                queue.appendleft(node.left)
            i += 1
            if i < len(flat_bt) and flat_bt[i]:
                node.right = TreeNode(int(flat_bt[i]))
                queue.appendleft(node.right)
            i += 1
        return ans
    
    def serialize(self, root) -> str:
        """
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        vals = []

        # preorder traversal
        def dfs(node):
            if not node: 
                vals.append("*")
            else:
                vals.append(str(node.val))
                dfs(node.left)
                dfs(node.right)

        dfs(root)

        # join on spaces for negative numbers, easier split
        return ' '.join(vals)

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        # defeault split on spaces
        vals = iter(data.split())

        # create the nodes in preorder traversal
        def dfs():
            tmp = next(vals)
            if tmp == '*':
                return None
            node = TreeNode(int(tmp))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))