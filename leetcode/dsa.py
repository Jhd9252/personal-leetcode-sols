

# %% [4] Basic Data Science Functions


# %% [5] Basic MatPlotLib Functions

#=============================================================



#=============================================================

#=============================================================


#%% [9] 2D Matrix / Grid  Examples

#=============================================================
    

#=============================================================


#=============================================================

# %% [11] Stack
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        if len(self.stack) == 0:
            raise IndexError('Empty stack')
        self.stack.pop()
    def peek(self):
        if self.is_empty():
            return None 
        return self.stack[-1]
    def is_empty():
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

#=============================================================

# %% [12] Heap and Methods
# - array that represents a binary tree

# min heap 
import heapq
minheap = []
heapq.heapush(minheap, 1)
heapq.heapush(minheap, 5)
heapq.heapush(minheap,, 2)
heapq.heappop(minheap)

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (idx -1) // 2

    def left_child(self, i):
        return 2*i+1

    def right_child(self, i):
        return 2*i+2

    def _sift_up(self, i):
        ''' After insertion to leaf '''
        parent = self.parent(i)
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent 
            parent = self.parent(i)

    def _sift_down(self, i):
        ''' After deletion '''
        while True:
            smallest = i 
            left = self.left(i)
            right = self.right(i)
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left 
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right 
            if smallest == i:
                break 
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def insert(self, data):
        self.heap.append(data)
        self._sift_up(len(self.stack) - 1)

    def delete_min(self, data):
        if not self.heap: return None 
        if len(self.heap) == 1: return self.heap.pop()
        # grab for return 
        root = self.heap[0]
        # replace min root with leaf, sift down 
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root 


    

#=============================================================
#=============================================================

# %% [13] Queue
# queue implementation in python
class Queue:
    def __init__(self):
        self.queue = []
    def __str__(self):
        return str(self.queue)
    def is_empty(): 
        return len(self.heap) <= 0
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Dequeue from empty queue')
        return self.queue.pop(0)
    def peek(self):
        if self.is_empty():
            raise IndexError('Peek at empty queue')
        return self.queue[0]
    def size(self):
        return len(self.queue)

#=============================================================

'''
[15] Binary Search Tree and Methods

A complete binary tree has at most n = 2^(h+1) - 1 nodes
'''
class TreeNode:
    def __init__(self, data, parent = None, left = None, right = None):
        self.data = data
        self.parent = parent 
        self.left = left 
        self.right = right 

class Tree:
    def __init__(self):
        self.root = None 

    # iterative
    def insert(self, data):
        # base case : no head 
        if not self.root:
            self.root = TreeNode(data)
        # insert as leaf 
        curr = self.root
        while True:
            if data < curr.val:
                if not curr.left:
                    curr.left = TreeNode(data)
                curr = curr.left 
            else:
                if not curr.right:
                    curr.right = TreeNode(data)
                curr = curr.right 
    # recurse
    def insert(self, root, data):
        # base case: reached null node
        if not root: 
            return TreeNode(data)

        # recurse
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        return root 

    def minimum(self, node=None):
        curr = self.root if not node else node 
        if not curr: return None 
        while curr.left:
            curr = curr.left:
        return curr 

    def maximum(self, node=None):
        curr = self.root if not node else node 
        if not curr: return None 
        while curr.right:
            curr = curr.right 
        return curr 

    def preorder(self, root=None):
        root = root if root else self.root
        if not root: return None 
        print(root.val, end = '>')
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root=None):
        root = root if root else self.root 
        if not root: return None 


    def preorder(self, root=None):
        root = root if root else self.root
        if root:
            print(root.val, end = '->')
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root=None):
        root = root if root else self.root
        if root is not None:
            self.inorder(root.left)
            print(root.val, end = '->')
            self.inorder(root.right)

    def postorder(self, root=None):
        root = root if root else self.root
        if root is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(root.val, end = '->')

    def get_node(self, data):
        if not self.root: return None 
        curr = self.root
        while curr and curr.val != data:
            if data < curr:
                curr = curr.left 
            else:
                curr = curr.right 
        return curr if curr.val == data else None 

    def parent(self, data):
        if not self.root:
            return None 

        if self.root.val == data:
            return None 

        curr = self.root 
        while curr:
            if curr.left == data or curr.right == data:
                return curr 
            else:
                if curr.val < data:
                    curr = curr.left 
                else:
                    curr = curr.right 
        return None 

    def predecessor(self, node):
        '''
        (1) If left subtree exists, go far right
        (2) If left subtree DNE, then ancestor that is right child, start from root 
        '''

        # case 1:
        if node.left:
            # return self.maximum(node.left)
            curr = node.left 
            while curr.right:
                curr = curr.right 
            return curr 

        # case 2: no parent tracking 
        pred = None 
        curr = self.root 
        while curr:
            if curr.val < node.left:
                pred = curr 
                curr = curr.right 
            elif curr.val > node.val:
                curr = curr.left 
            else:
                break

        # case 2: parent tracking, find when curr is a right child -> return parent
        curr = node 
        while curr.parent and curr == curr.parent.left:
            curr = curr.parent 
        return curr.parent 

    def successor(self, node):
        '''
        (1) Right subtree exists, left most node
        (2) Right subtree DNE, parent of ancestor who is left child
        (3) In order traversal to find node -> next visited node
        '''
        # right subtree exists
        if node.right:
            return self.minimum(node.right)

        # right subtree DNE, no parent tracking
        sucessor = None 
        curr = self.root 
        while curr:
            if curr.val > node.val:
                sucessor = curr 
                curr = curr.left 
            else:
                curr = curr.right 
        return curr 

    def delete(self, data):
        ''' Iterative delete '''

        # initialize 
        parent = None 
        curr = self.root 

        # check initialize
        if not curr:
            raise IndexError()

        # find the node to delete while update parent
        while curr and curr.val != data:
            parent = curr 
            if data < curr.val:
                curr = curr.left 
            else:
                curr = curr.right 

        if not curr:
            raise IndexError()

        # case 1 and 2: [0,1] child
        if not curr.left or not curr.right:
            child = curr.left if curr.left else curr.right 
            # edge case if curr is root with no parent
            if not parent:
                self.root = child 
            elif parent.left == curr:
                parent.left = child 
            else:
                parent.right = child 
            return self.root 

        # case 3: two children
        succ = self.successor(curr)
        curr.val = succ.val 
        self.delete(succ.val)
        return self.root 

    def delete(self, node, data):
        ''' Recursive delete '''
        if not node or not data: 
            return None 

        if key < node.val:
            node.left = self.delete(node.left, data)
        elif key > node.val:
            node.right = self.delete(node.right, data)
        else:
            # found node to delete

            # case 1 and 2
            if not node.left or not node.right:
                subtree = node.left if node.left else node.right 
                return subtree 

            # case 2 
            succ = self.successor(node)
            node.val = succ.val 
            node.right = self.delete(node.right, succ.val)
        return node 

    def search_iterative(self, data):
        if not self.root:
            return False
        curr = self.root 
        while curr and curr.val != data:
            if data < curr.val:
                curr = curr.left 
            else:
                curr = curr.right 
        return True if curr != self.root else False


    def search_recursive(self, node, data):
        # termination case
        if not node:
            return False
        if node.val == data:
            return True 
        # recursion
        if data < node.val:
            # return action
            return self.search_recursive(node.left, data)
        else:
            # return action 
            return self.search_recursive(node.right, data)

    def bfs_depth(self, root=None):
        ''' Iterative'''
        if not root: return 0

        q = deque([root])
        depth = 0

        while q:
            qLen = len(q)
            for _ in range(qLen):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
        return depth 

    def dfs_depth(self, root = None):
        ''' DFS iterative with stack'''
        if not root: return 0 
        depth = 1 
        stack = [(root, 1)]

        while stack:
            node, level = stack.pop()
            if node:
                depth = max(depth, level)
                stack.append((node.left, level + 1))
                stack.append((node.right, level + 1))
        return depth 

    def dfs_depth(self, root):
        ''' Dfs recursive '''
        # base case
        if not root: return 0 
        # at this level, recurse both paths, get the max, add 1, return 
        return 1 + max(self.dfs_depth(root.left), self.dfs_depth(root.right))

    def bfs_width(self, root):
        ''' BFS with (node, pos, level) '''
        width = 0
        q = deque([root, 1, 0])
        prevLevel, posFirst = 0, 1

        while q:
            node, pos, level = q.popleft()
            if prevLevel < level:
                prevLevel = level 
                posFirst = pos 
            width = max(width, pos - posFirst + 1)

            if node.left:
                q.append([node.left, pos * 2, level + 1])
            
            if node.right:
                q.append([node.right, pos*2+1, level + 1])
        return width 

    def maxPathSum(self, root):
        '''
        DFS
        Path does not need to contain root. 
        At every node, we calculate as if splitting, set the result then pass up as single
        '''
        res = [root.val]
        def dfs(root):
            if not root: return 0 

            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))

            res[0] = max(res[0], root.val + left + right)

            return root.val + max(left right)
        dfs(root)
        return res[0]

    def bfs_level(self, root):
        if not root: return []
        orders = []
        q = deque([root])

        while q:
            qLen = len(q)
            level = []
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                order.append(level)
        return orders

    def LCA(self, A, B):
        '''
        Lowest common ancestor
        (1) Look into both subtrees starting from the root
        (2) Find the if both < root, then not, travel
        (2) Find the if both > root, then not, travel
        (3) Nodes can be an ancestor to itself 
        '''

        curr = root
        while curr:
            if A.val < curr.val and B.val < curr.val:
                curr = curr.left 
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right 
            else:
                return curr
        return None 

    def invert(self, root):
        '''
        BFS Queue 
        '''
        q = deque([root])
        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left 
            if node.left: q.apend(node.left)
            if node.right: q.append(node.right)
        return root 

    def invert(self, root):
        ''' DFS '''
        if not root: return root 
        root.left, root.right = self.invert(root.right), self.invert(root.left)
        return root 
            






#=============================================================














# %% [16] RB-Tree
'''
Red Black Tree and Methods

Four Properties:
(1) Root and leaf is black -> sentinent Node 
(2) Every node has a color attribute
(3) If a node is red, both children must be black
(4) For every node, all simple paths from node to leaf contains the same number of black nodes 

Height of at most 2log(n+1)

Special RB Operations: 
(1) Insertion: Standard BST operation, default color is red. Depending, rotate and/or recolor
(2) Deletion: More complicated than insertion. Use Translant, and delete_fixup depending on case after deletion
(3) Recolor
(4) Left and right rotate: restructure a tree with breaking BST. Changing links, not colors. 
    Left(BST, PivotNode) -> only works if node's right subtree is non-empty
    Right(BST, PivotNode) -> only works if node's left subtree is non-empty
(5) Transplant
(6) delete_fixups: changes colors and performs rotations to restore RB properties

Applications and Advantages
(1) Efficient implementation of associate arrays
(2) Efficient implementaion of priority queues
(3) Efficient implementation of dynamic set operations 

Violations when inserting a node into RB tree
(1) If the root node is being inserted -> New root node must be black
(2) If the parent node is black -> you can insert as red node
(3) If the parent is red node: assume inserted is black
    (3A) Uncle is red: recolor inserted node and parent to black, grandparent to red, fix violations upwards
    (3B) Uncle is black (or null)
        (LL): If new node is left child, perform right rotation on grandparent
        (LR): If new node is right child, perform left rotation on parent, and right rotation on grandparent
        (RR): If new node is right chidl, perform left rotation on grandparent
        (RL): If new node is left child, perform right rotation on parent and left rotation on grandparent
(4) After fixing violations, ensure root is black
'''
      
def rotate_left(self, u):
    # assign a label to right child
    v = u.right 

    # Step 1 Bottom : Break node right link -> assign to v.left both ways
    u.right = v.left 
    if v.left != self.nil:
        v.left.parent = u 

    # Step 2 Top: change v's parent to u's parent
    if u.parent is None:
        self.root = v
    elif u.parent.left == u:
        u.parent.left == v 
    else:
        u.parent.right = v 

    # step 3 Mid: Final change
    v.left, u.parent = u, v 

from redblacktree import rbtree
tree = rbtree([1, 2, (3, 'three'), 4])
tree.insert(5, 'five')
print(tree[3])  # Output: 'three'


# can also insert key:values
from redblacktree import rbtree
tree = rbtree([1,2,(3, 'three'), 4])
tree.insert(5, 'five')
print(tree[3])
#=============================================================
'''
B-Tree
Each node has ascending [key1, key2, key3, ...]
Each node has children = 1 + numKeys

All leafs are at the same level 
HeightMax = ceil(log(n+1)) - 1
HeightMix = floor(log((n+1)/2))

Every node has min and max number of keys
    - Minimum is always half
    - Maximum is user defined

Inserts are at the bottom of the tree
    - If max keys and split needed, split into 2, push middle key to parent
    - Splitting is recursive 

Deletes can result in merges or taking from parent for separators.
'''
class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []      # 2t-1
        self.children = []  # 2t

    def display(self, level=0):
        print(f"Level {level}: {self.keys}")
        if not self.leaf:
            for child in self.children:
                child.display(level + 1)


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    def display(self):
        self.root.display()

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.children.append(root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(None)  # Make space for the new key
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.children[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.children[i]
        z = BTreeNode(leaf=y.leaf)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.children = y.children[t: 2 * t]
            y.children = y.children[0: t - 1]
        x.children.insert(i + 1, z)


    def main():
        B = BTree(3)

        keys = [10, 20, 5, 6, 12, 30, 7, 17]
        for key in keys:
            B.insert(key)

        print("B-tree structure:")
        B.display()

#=============================================================
from BTrees.OOBTree import OOBTree
btree = OOBTree()
btree['apple'] = 1
btree['banana'] = 2
b.update({3:'black', 4: '333'})
print(btree['apple'])  # Output: 1

keys = btrees.keys()
len(keys)
vals = btree.values()
vals = brtee.values(min=1, max=32)
vals = btree.values(min=1, max =32, excludemin = True, excludemax =True)
minkey = btree.minKey()
minkey = btree.minKey(2) # <= 2
for pair in btree.iteritems():
    print(pair)
print(btree.has_key(3))

#=============================================================
# %% [18] Trie (Pre-fix for string building) and Methods
###############################################################################################
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root 
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True 

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False 
            node = node.children[char]
        return node.end 

    def starts_with(self, prefix):
        node = self.root
        for char in word:
            if char not in node.children:
                return False 
            node = node.children[char]
        return True 


#=============================================================
'''
Graph and Algorithms
    - Graphs are connected when all vertices are reachable from each other.
    - Graphs are not connected when more than one component for less than n-1 edges
'''
class Graph:
    def __init(self):
        self.v = set()
        self.e = []

    def add_vertex(self, v):
        self.v.add(v)

    def remove_vertex(self, vertex):
        if v in self.v:
            self.v.remove(vertex)
            self.e = [(u,v,w) for u,v,w in self.e if u!=vertex and v!=vertex]

    def add_edge(self, u, v, weight):
        if u in self.v and v in self.v:
            self.e.append((u,v,w))

    def remove_edge(self, u, v):
        self.e = [(x,y,z) for x,y,z in self.e if (x,y) != (u,v) and (x,y) != (v,u)]

#=============================================================
def bfs(graph: dict, root):
    if not graph or not root: return 
    res = []
    visited = set()
    q = deque([root])

    while q:
        node = q.popleft()
        if node in visited:
            continue 
        visited.add(node)
        res.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                q.append(neighbor)
    return res

def dfs(graph: dict, root):
    if not graph or root not in graph:
        return []

    visited = set()
    stack = [root]
    res = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        res.append(node)

        # Push neighbors in reverse order if you want left-to-right traversal
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

    return res

def dfs(graph: dict, visited = None, root):
    ''' DFS recursion '''

    if not graph or not root: return 

    # process this current node
    if visited is None:
        visited = set()
    visited.add(root)

    # preprocess / create result 
    res = [root]

    # recurse 
    for neighbor in graph[root]:
        if neighbor not in visited:
            res += dfs(graph, visited, neighbor)

    return res 

#=============================================================
import networkx as nx 
graph = nx.DirGraph()
graph.add_edges_from([(1,2)])
topo_order = list[nx.topological_sort(graph)]

def topologicalSort(graph: dict):

    visited = set()
    order = []

    def dfs(node):
        visited.add(node)
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in graph:
        if node not in visited:
            dfs(node)

    return order 

def topologicalSort(graph:dict):
    # with cycle detection

    visiting = set()
    visited = set()
    finish = []

    def dfs(node):
        # base case
        if node in visiting: return False # cycle
        if node in visited: return True # already processed

        # process this node
        visiting.add(node)

        for neighbor in graph.get(node, []):
            if not dfs(neighbor):
                return False

        # post process
        visiting.remove(node)
        visited.add(node)
        finish.append(node)

        return True 

    for node in graph:
        if node not in visited:
            if not dfs(node):
                return []
    return finish[::-1]


def kahnsTopologicalSort(edges: list[tuple]):
    # convert to adj list if needed
    graph = collections.defaultdict(list)
    degree = collections.defaultdict(int)

    # create (NOTE: disconnected components also have a source)
    for u, v in edges:
        graph[u].append(v)
        degree[v] += 1

    # start
    queue = deque([node for node in graph if degree[node] == 0])

    res = []

    while queue:
        node = q.popleft()
        res.append(node)
        for neighbor in graph[node]:
            degree[neighbor] -= 1
            if degree[neighbor] == 0: 
                queue.append(neighbor)
    return res




#=============================================================
# SCCS kosarajus DFS to populate the finish stack, transpose, DFS on transpose

def dfs(graph: dict, node, visited:set = None, stack:list=None, component:list=None):

    # instantiate if not 
    if not visited: visited = set()

    # process this node 
    visited.add(node)

    # component step
    if component is not None: component.append(node)

    # recursion
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack, component)

    # post process - first step
    if stack is not None: stack.append(node)

def transpose(graph:dict) -> dict:
    tmp = collections.defaultdict(list)

    for node in graph:
        for neighbor in graph[node]:
            tmp[neighbor].append(node)
            # make sure source nodes are recorded
            if node not tmp: tmp[node] = []

    return tmp


def kosaraju(graph: dict) -> list:
    # step 1: dfs to populate the stack
    visited = set()
    stack = []
    for node in graph:
        if node not in visited:
            dfS(graph, node, visited, stack=stack)

    # step 2: transpose the edges
    transposed = transpose(graph)

    # step 3: DFS on transpose in reverse finish times
    visited = set()
    sccs = []
    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs(transposed, node, visited, component=component)

    return sccs


def tarjans(graph: dict):
    # instantiate
    discover = 0
    lowlink = {}
    index = {}
    stack = []
    onstack = set()
    sccs = []

    def scc(node):
        # preprocess
        nonlocal discover
        index[node] = discover
        lowlink[node] = discover
        discover += 1
        stack.append(node)
        onstack.add(node)

        # recursion
        for neighbor in graph[node]:
            if neighbor not in index:
                scc(neighbor)
                lowlink[node] = min(lowlink[node], lowlink[neighbor])
            elif neighbor in onstack:
                lowlink[node] = min(lowlink[node], index[neighbor])

        # post process -> check if source
        if lowlink[node] == index[node]:
            component = []
            while True:
                tmp = stack.pop()
                onstack.remove(tmp)
                component.append(tmp)
                if tmp == node:
                    break
            sccs.append(component)
    for node in graph:
        if node not in index:
            scc(node)

    return sccs

#=============================================================
'''
Dikstas SSSP: BFS with MINPRIO
Input: DAG (undirected create two edges) with non-negative weights
Output: Distance hashmap {node : (dist from source, parent)
Process: Start from root, use minprio for lowest edge (cost, node), add updated edges
Runtime: O((V+E)LogV) = O(logV) heappop, O(logvE) pushes
Space: O(V+E)
'''

import heapq
def dijkstras(graph: dict, root) -> dict:
    # create distance hashmap {node: (dist from source, parent)}
    dist = {node: (float('inf'), None) for node in graph}
    dist[root] = (0, None)

    # create minHeap for next lowest cost edge of a discovered node
    minHeap = [(0, root)]

    while minHeap:
        cost, node = heapq.heappop(minHeap)

        # Skip outdated entries
        if cost > dist[node][0]:
            continue

        # Relax edges
        for w, neighbor in graph.get(node, []):
            if cost + w < dist[neighbor][0]:
                dist[neighbor] = (cost + w, node)
                heapq.heappush(minHeap, (cost + w, neighbor))

    return dist

def rebuildPath(distances: dict, last):
    path = []
    while last != None:
        path.append(last)
        last = dist[last][1]
    return path[::-1]

#=============================================================
'''
SSSP Bellman Fords : Negative weights, Cycle detection, Relax all edges
Input: DAG, negative weights
Output: Distance hashmap
Runtime: O(VE)
Space: O(V+E)
'''
def bellmanFord(graph: dict, root) -> dict:
    dist = {node: (float('inf'), None) for node in graph}
    dist[root] = (0, None)

    # for every count of node, for every edge, relax
    for _ in range(len(graph)):
        for node in graph:
            for weight, neighbor in graph[node]:
                curr = weight + dist[node][0]
                if curr < dist[neighbor][0]:
                    dist[neighbor] = (curr, node)

    # detect cycle if needed
    for node in graph:
        for weight, neighbor in graph[node]:
            if dist[node][0] + weight < dist[neighbor][0]:
                raise ValueError()


    return dist 

def rebuild(dist, last):
    path = []
    while last != None:
        path.append(last)
        last = dist[last][1]
    return path[::-1]

#=============================================================
# cycle detection

# undirected graph
def has_cycle(graph):
    ''' If visited and not parent '''
    visited = set()
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
    for node in graph:
        if node not in visited:
            if explore(node, None):
                return True
    return False 

# directed graph
def has_cycle(graph: dict):
    visited = set()
    stack = set()

    def dfs(node):
        visited.add(node)
        stack.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in stack:
                return True
        stack.remove(node)
        return False 
    for node in graph:
        if node not in visited:
            if dfs(node): 
                return True
    return False




# negative weight cycle -> Bellman fords final cycle

#=============================================================
'''
Floyd Warshall APSP: Intermediate Vertex
Input: Adjlist or Matrix -> requires index or index mapping
Output: 2D matrix of shortest paths of all pairs where dist[i][j] is shortest dist from i to j
Idea: Treat each node as middle man between all other pairs
Runtime: O(V**3)
Space: O(V**2)
'''

# given adjlist
def floydWarshall_apsp(graph: dict):
    # convert graph {node: (w, neighbor)}
    nodes = list(graph.keys())
    for edges in graph.values():
        for weight, neighbor in edges:
            if neighbor not in nodes:
                nodes.append(neighbor)
    # create mappers both ways
    V = len(nodes)
    node_index = {node: i for i, node in enumerate(nodes)}
    index_node = {i: node for i, node in enumerate(nodes)}
    # initialize 2D distance array using mapped index
    dist = [[float('inf') for i in range(V)] for j in range(V)]
    # initialize all dist from node to itself as zero
    for i in range(V):
        dist[i][i] = 0
    # fill in the rest of the distances
    for node in graph:
        i = node_index[node]
        for weight, neighbor in graph.get(node, []):
            j = node_index[neighbor]
            dist[i][j] = weight 
    # floyd 
    for mid in range(V):
        for start in range(V):
            for end in range(V):
                if dist[start][mid] + dist[mid][end] < dist[start][end]:
                    dist[start][end] = dist[start][mid] + dist[mid][end]

    return dist, node_index, index_node


# given adjmatrix(graph):
def floydwarshall_apsp(graph: list[list[int]]):
    V = len(graph)
    dist = [[float('inf') for i in range(V)] for j in range(V)]

    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]

    for i in range(V):
        dist[i][i] = 0

    for y in range(V):
        for x in range(V):
            for z in range(V):
                if dist[x][y] + dist[y][z] < dist[x][z]:
                    dist[x][z] = dist[x][y] + dist[y][z]

    for i in range(V):
        if dist[i][i] < 0:
            raise ValueError()

    return dist 


#=============================================================
# using dijkstras for apsp is O((V+E)logV) * V

# DIJkstras is O((V+E)logV)
# APSP with dijkstra is O((V+E)logV * V))
def dijkstra(graph, root):
    dist = {node: (float('inf'), None) for node in graph}
    dist[root] = (0, None)

    minprio = [(0, root)]

    while minprio:
        curr_dist, node = heapq.heappop(minprio)
        if curr_dist > dist[node][0]:
            continue
        for weight, neighbor in graph[node]:
            if curr_dist + weight < dist[neighbor][0]:
                dist[neighbor] = (curr_dist + weight, node)
                heapq.heappush(minprio, (curr_dist+weight, neighbor))
    return dist 

def APSP_dijkstra(graph):
    apsp = {}
    for node in graph:
        apsp[node] = dijkstra(graph, node)
    return apsp 

def reconstruct_path(apsp, start, end):
    path = []
    current = end
    while current is not None and current != start:
        path.append(current)
        current = apsp[start][current][1]
    if current is None:
        return None  # no path
    path.append(start)
    return path[::-1]

#=============================================================

'''
Prims: MST algorithm using BFS, min priority queue, connected graphs

Does Prim's require a root node? → ✅ Yes.
Does the choice of root affect the final MST? → ❌ No (for connected graphs).

Intuition:
(1) Initialize a empty MST edge set, visited set, heap
(2) starting from an arbitrary, greedily select lowest cost edge
(3) add that edge to list and add all other connecting edges that is unvisited
(4) repeat

Runtime: O(ElogV)


'''
'''
Prims MST: BFS, minprio queue, greedy, connected
RT: O(ElogV)
Space: O(V)

Intuition:
(1) start with empty visited set, edge list, root
(2) start with (0, root, None), find safe outgoing edge
(3) add that edge to list
(4) add all outgoing edges from destination node that is unvisited to q
(5) repeat

'''

import heapq
def primsMST(graph, root):
    MST = []
    visited = set()
    minheap = [(0, root, None)]

    while minheap:
        cost, node, parent = heapq.heappop(minprio)

        if node in visited:
            continue

        visited.add(node)

        if parent is not None:
            MST.append((parent, node, cost))

        for weight, neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(minheap, (weight, neighbor, node))
    return MST


#=============================================================


'''
Kruskal MST: MST using union find
RT: O(ElogV)
Space: O(E)

Idea:
(1) Create mapping from node <-> ID if needed
(2) empty edge list
(3) empty edge list -> add and sort
(4) empty parent list
(5) define find (parent: dict, node) with path compression
(6) define union (parent: dict, node, neighbor) 
    - find parent
    - if not same, join and return boolean
(7) for each edge (u,v) in sorted edges
    - use union find and attempt add edge
    - if succesful, add edge to MST set
(8) return 
'''
def krusaklMST(graph):
    def find(parent:dict, node):
        if parent[node] != node:
            parent[node] = find(parent, parent[node])
        return parent[node]

    def union(parent: dict, A, B):
        p1 = find(parent, A)
        p2 = find(parent, B)
        if p1 != p2:
            parent[p1] = p2 
            return True 
        return False

    node_index = {}
    index_node = {}
    index = 0
    for node in graph:
        if node not in index_node:
            node_index[node] = index 
            index_node[index] = node 
            index += 1
    MST = []
    parent = {i: i for i in range(index)}
    edges = []
    seen = set()
    for node in graph:
        nodeidx = node_index[node]
        for (weight, neighbor) in graph[node]:
            neighboridx = node_index[neighbor]
            if (weight, nodeidx, neighboridx) not in edges:
                edges.append((weight, nodeidx, neighboridx))
    edges.sort()

    for (weight, nodeidx, neighboridx) in edges:
        if union(parent, nodeidx, neighboridx):
            MST.append(weight, nodeidx, neighboridx)

    return MST 





#=============================================================
# %% [23] Flow Network & Max Flow Problems 
"""
Flow Network, Maximum Flow Problem

Input: Adjacency Matrix

Residual Graph:
(1) Forward edges are potential capacity left to push
(2) Backward edges are capacities that we want take back. 
NOTE: Then forward edge and backward edge from A->B must be max flow.

(1) Start with zero flow in network
(1) While there is an augmenting path (either forward while tracking parent)
(2) Find the minimum bottleneck on that path
(3) Update the flow with value, add to maxflow
    - When you add flow from source to sink
    - You decrease flow from sink to source
(4) Repeat

"""

from collections import deque
def bfs(residual, source, sink, parent: dict) -> bool:
    '''
    Find an augmenting path from source to sink (forward edges)
    Track parents
    Return path exists - boolean
    '''
    visited = set()
    queue = deque([source])
    parent.clear()

    while queue:
        node = queue.popleft()
        for capacity, neighbor in enumerate(residual[node]):
            if neighbor not in visited and capacity > 0:
                visited.add(neighbor)
                parent[neighbor] = node
                if neighbor == sink:
                    return True 
                queue.append(neighbor)
    return False 


def FFMF(graph, source, sink):

    n = len(graph)
    residual = [row[:] for row in graph]
    maxFlow = 0
    parent = {}

    while bfs(residual, source, sink, parent):

        # find the bottleneck (we can only augment by least)
        pathFlow = float('-inf')
        v = sink 

        while v != source:
            u = parent[v]
            pathFlow = min(pathFlow, residual[u][v])
            v = u

        # update capacities in both directions
        v = sink 
        while v != sink:
            u = parent[v]
            residual[u][v] -= pathFlow
            residual[v][u] += pathFlow
            v = u 

        # update overall flow
        maxFlow += pathFlow
    return maxFlow 

 
#======================================================================
def backtrack(curr, others):
    if (BASE_CASE):
        # do something  / append answer
        return ans 

    # otherwise, continue exhausting
    ans = 0
    for (iterate over further input):
        ans += backtrack(params)
    return ans 


def generateParenthesis(n:int):
    ''' Given n-pairs, generate all possible combinations of well formed parenthesis '''
    res = []
    stack = []
    def backtrack(res, stack, n, left, right):
        # base case 
        if left == right == n:
            res.append(''.join(stack))

        # otherwise, recurse according to condition
        if left < n:
            stack.append('(')
            backtrack(res, stack, n, left+1, right)
            stack.pop()
        if right < left:
            stack.append(')')
            backtrack(res, stack, n, left, right + 1)
            stack.pop()

        return res 



#======================================================================
# DP Top Down with memoization (repeated calls)

def fn(arr):
    memo = {}
    def dp(STATE):
        if BASE_CASE:
            return 0
        if STATE in memo:
            return memo[STATE]
        ans = RECURRENCE_RELATION(STATE)
        memo[state] = ans 
        return ans 
    return dp(STATE_FOR_WHOLE_INPUT)

def fib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def fib(n:int):
    memo = {}
    def dp(STATE):
        if STATE == 0: return 0
        if STATE == 1: return 1
        if STATE == 2: return 1
        if STATE in memo:
            return memo[STATE]
        memo[STATE] = dp(n-1) + dp(n-2)
        return memo[state]
    return dp(n)

def fib(n: int):
    prev, curr = 1, 1
    for i in range(2, n+1):
        tmp = prev + curr 
        prev, curr = curr, tmp 
    return curr 

# dynamic programming outline: top down memoization
def fn(arr):
    memo = {}
    def dp(STATE):
        if BASE_CASE:
            return 0
        if STATE in memo:
            return memo[state]
        ans = RECURRENCE_RELATION(STATE)
        memo[state] = ans 
        return ans 
    return dp(WHOLE_STATE)





#======================================================================
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance  

instance1 = Singleton()
instance2 = Singleton()

print(instance1 == instance2)
print(instance1 is instance2)
#======================================================================
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass 
class Dog(Animal):
    def speak(self):
        print('meow')



#======================================================================
Exact Match:                        left <= right, left = mid + 1, right = mid - 1
First Occurence / Left convergence  left < right, left = mid + 1, right = mid 
last occurence / right convergence  left < right, left = mid, right = mid - 1


#======================================================================
def recursion():
    # 3. base case: stop recrusing and return soemthing fundamental

    # 1. preprocessing stage ? head stage as we go down

    # 2. recursion stage / process of going down 

    # 4. post process / assignement / checks

    # 5. return upwards to post process of previous level 

#======================================================================
pip install kmp-algorithm
from kpm install KPMMatcher
matcher = KMPMatcher(substring)
index = matcher.search(string) # return start index if found else -1 


#======================================================================
def lps(substring):
    m = len(substring)
    lps = [0] * m 
    left = 0 # length
    for right in range(1, m):

        # NOTE: This part tells the algorithm what to do if the chars dont match -> left goes back to the prev recorded
        # Fall back in the array until we find a match, or reach zero
        while substring[left] != substring[right] and left > 0:
            left = lps[left-1] # backtrack to the prev matched prefix
        # NOTE: IF the chars match, then move left and set lps[right] = left 
        if substring[right] == substring[left]:
            left += 1
            lps[right] = left 
    return lps 

def kmp(string, substring): 
    n, m - len(string, substring):
    lps = lps(substring)
    res = []
    left = 0

    # ranging over the original string
    for right in range(n):

        # if no match, fall back left pointer until match or zero
        while string[right] != substring[left] and left > 0:
            left = lps[left - 1]

        # if match, then increment left 
        if string[right] == substring[left]:
            left += 1

            # we do not set the array like in LPS, the lps is already set
            # if there is a match, we increment and check if full pattern found
            if left == m:
                res.append(right) 

    return res if res else -1 





#======================================================================