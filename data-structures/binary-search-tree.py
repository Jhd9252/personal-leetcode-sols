import collections

class Node:
    def __init__(self, data, parent = None, left = None, right = None):
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data
class BST:
    def __init__(self):
        self.root = None 

    def insert(self, data):
        ''' Iterative O(logn) '''

        # edge case - no root
        if not self.root: self.root = Node(data)

        curr = self.root
        while True:
            if data < curr.data:
                if not curr.left:
                    curr.left = Node(data)
                    return 
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = Node(data)
                    return 
                curr = curr.right 
        
    def insert(self, data, root):
        ''' Recursive O(logn), Space O(logn)'''
        # base case 1
        if not self.root: 
            self.root = Node(data)
            return 
        # base case 2: current node does not exist
        if not root: return Node(data)
        if data < root.data:
            root.left = self.insert(data, root.left)
        else:
            root.right = self.insert(data, root.right)
        return root 
        
    def minimum(self, root = None):
        curr = self.root if not root else root
        if not curr: return None
        while curr.left:
            curr = curr.left
        return curr 
    
    def maximum(self, root = None):
        curr = self.root if not root else root
        if not curr: return None
        while curr.right:
            curr = curr.right
        return curr 
    
    def preorder(self, root = None):
        root = root if root else self.root 
        if root:
            print(root.val, end = '->')
            self.preorder(root.left)
            self.preorder(root.right)
    
    def inorder(self, root = None):
        root = root if root else self.root
        if root:
            self.inorder(root.left)
            print(root.val, end = '->')
            self.inroder(root.right)
    
    def postorder(self, root = None):
        root = root if root else self.root
        if root:
            self.postoder(root.left)
            self.postorder(root.right)
            print(root.data, end = '->')

    def search(self, data):
        if not self.root: return None
        curr = self.root
        while curr and curr.data != data:
            if data < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return curr if curr and curr.data == data else None
    
    def parent(self, data):
        if not self.root: return None
        if self.root.data == data:
            return None
        curr = self.root
        while curr:
            if curr.left == data or curr.right == data:
                return curr
            else:
                if data < curr.data:
                    curr = curr.left 
                else:
                    curr = curr.right
        return None
    
    def predecessor(self, node):

        # case 1: left subtree exists -> get max
        if node.left:
            curr = node.left
            while curr.right:
                curr = curr.right
            return curr
        
        # case 2: no left subtree, ancestor, who is also a right child from root 
        pred = None
        curr = self.root
        while curr:
            if curr.data < node.data:
                pred = curr
                curr = curr.right
            elif curr.data > node.data:
                curr = curr.left 
            else:
                break
        return pred
    
    def successor(self, node):
        # case 1 - right subtree exists
        if node.right:
            curr = node.right
            while curr.right:
                curr = curr.right
            return curr 
        
        # case 2 - no right subtree, get ancestor who is greater
        succ = None
        curr = self.root
        while curr:
            if curr.data > node.data:
                succ = curr
                curr = curr.left
            elif curr.data < node.data: 
                curr = curr.right
            else:
                break
        return succ 
    
    def delete(self, data):
        ''' Iterative '''
        # base case: no root
        parent = None 
        curr = self.root
        if not curr: return None 

        # find child to delete
        while curr and curr.data != data:
            parent = curr 
            if data < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        # if current pointer is no longer valid, in BST, data does not exists
        if not curr: return None

        # otherwise, curr is not None, we found data to delete

        # case 1: no children -> delete
        # case 2: 1 child -> elevate
        # case 3: 2 children
        if not curr.left or not curr.right:
            child = curr.left if curr.left else curr.right
            # if root 
            if not parent:
                self.root = child 
            elif parent.left == curr:
                parent.left = child
            else:
                parent.right = child 
        
        # case 3: 2 children -> succesor
        succ = self.successor(data)
        curr.data = succ.data
        self.delete(succ.data)
        return self.root
    
    def delete(self, node, data):
        ''' Recursive '''

        if not node or not data: return None
        if data < node.data:
            node.left = self.delete(node.left, data)
        elif data > node.data:
            node.right = self.delete(node.right, data)
        else:
            # found node to delete
            # case 1 and 2
            if not node.left or not node.right:
                subtree = node.left if node.left else node.right
                return subtree
            
        return node 
    
    def search(self, data):
        ''' Iterative -> return node'''
        if not self.root: return None
        curr = self.root 
        while curr and curr.data != data:
            if data < curr.data:
                curr = curr.left 
            else:
                curr = curr.right

        # return True if curr else False 
        return curr if curr else None
            
    


    
    
    def depth(self, root = None):
        ''' BFS'''
        if not root: return 0
        root = root if root else self.root
        if not self.root: return 0
        res = 0
        q = collections.deque([root])
        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res += 1
        return res 
    
    def depth(self, root = None):
        ''' DFS Stack '''
        res = 0
        stack = [(root, 1)]

        while stack:
            node, level = stack.pop()
            if node:
                res = max(res, level)
                stack.append((node.left, level + 1))
                stack.append((node.right, level + 1))
        return res
    

    def depth(self, root = None):
        ''' DFS recursive '''
        if not root: return 0
        
        return 1 + max(self.dfs(root.left), self.dfs(root.right))
    
    def width(self, root = None):
        ''' BFS with labeled positions according to position 1 - indexed '''
        width = 0
        queue = collections.deque([(root, 1, 1)]) # (node, level, pos)
        prevLevel = 1, firstPos = 1
        while queue:
            node, level, pos = queue.popleft()
            if prevLevel < level:
                prevLevel = level
                firstPos = pos
            width = max(width, pos - firstPos + 1)
            if node.left:
                queue.append((node.left, level + 1, 2*pos))
            if node.right:
                queue.append((node.right, level + 1, 2*pos + 1))

        return width
    
    def maxPathSum(self, root = None):
        root = root if root else self.root
        res = [root.data]

        # at each level, (1) treat as splitter (2) pass max up
        def dfs(node):
            # base case
            if not root: return 0
            left = max(0, self.dfs(node.left))
            right = max(0, self.dfs(node.right))
            res[0] = max(res[0], node.val + left + right)
            return node.val + max(left, right)
        dfs(root)
        return res[0]
    
    def levelOrder(self, root=None):
        root = root if root else self.root
        ''' BFS '''
        levels = []
        q = collections.deque([root])
        while q:
            qLen = len(q)
            tmp = []
            for _ in range(qLen):
                node = q.popleft()
                tmp.append(node)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if tmp: levels.append(tmp)
        return levels
    
    def LCA(self, A, B, root = None):
        root = root if root else self.root
        curr = root
        while curr:
            if A.data < curr.data and B.data < curr.data:
                curr = curr.left
            elif A.data > curr.data and B.data > curr.data:
                curr = curr.right
            else:
                # curr is one of A or B
                # curr splits A and B
                return curr
    
    
    def invert(self, root = None):
        root = root if root else self.root 
        curr = root
        if not curr: return 
        ''' BFS Queue '''
        q = collections.deque([curr])
        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return root 
    
    def invert(self, root = None):
        if not root: return root
        root.left, root.right = self.invert(root.right), self.invert(root.left)
        return root
    
    

        
