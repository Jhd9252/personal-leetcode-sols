'''
B-Tree

1. Each node as ascending [key1, key2,...]
2. Each node as children = 1 + numKeys

All leafs are at the same level
HeightMin = ceil(log(n+1)) - 1
HeightMAx = floor(log((n+1)/2 )

Every node has min and max number of keys: 
    - minimum is always half
    - maximum is user defined

Inserts occur at the bottom of the tre
    - if max keys and split is needed, split node into two nodes, push the middle key to parent 
    - splitting is done recursively 

deletes can result in merges or takin gfrom parent for separators
'''

class BTreeNode:
    def __init__(self, leaf = True):
        self.leaf = leaf 
        self.keys = []      # 2t-1
        self.children = []  # 2t

    def display(self, level = 0):
        print(f'Level {level}: {self.keys}')
        if not self.leaf:
            for child in self.children:
                child.display(level + 1)

class BTree:
    def __init__(self, t: int):
        self.root = BTreeNode(True)
        self.t = t
    
    def display(self):
        self.root.display()

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            tmp = BTreeNode()
            self.root = tmp
            tmp.children.append(root)
            self.split_child(tmp, 0)
            self.insert_nonfull(tmp, k)
        else:
            self.insert_nonfull(root, k)
        
    def insert_nonfull(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(None) # make space for new key
            while i >= 0 and k < x.keys[i]:
                x.keys[i+1] = x.keys[i]
                i -= 1
            x.keys[i+1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == (2*self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_nonfull(x.children[i], k)
    
    def split_child(self, x, k):
        t = self.t
        y = x.children[i]
        z = BTreeNode(leaf = y.leaf)
        x.keys.insert(i, y.keys[t-1])
        z.keys = y.keys[t: (2*t)-1]
        y.keys = y.keys[0:t-1]
        if not y.leaf:
            z.children = y.children[t:2*t]
            y.children = y.children[0:t-1]
        x.children.insert(i+1, z)

    
from BTrees.OOBTree import OOBTree

btree = OOBTree()
btree['apple'] = 1
b.update({3:'black', 4:'333'})
print(btree[apple])


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