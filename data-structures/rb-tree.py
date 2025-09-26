'''
RB Tree

Four Properties:
(1) Root and leaves are black -> sentinel node
(2) reveryu node ahs a color attribute
(3) if a node is red, both children must be black
(4) for every node, all simple paths from root to node contains same number of black nodes

Height of tree is at most 2log(n+1)

Special RB Operations
(1) Insertion: Standard BST operation. Default color is red. Depending, rotate and/or fixup
(2) Deleteion: More complicated than insertion. Use transplant(), delete_fixup() depending. 
(3) Recolor()
(4) Left and right rotate: restructures a tree with breaking BST. Changing links, not colors
    Left (BST, pivot node) -> only works if node's right subtree is non-empty
    Right (BST, pivot node) -> only works if node's left subtree is non-empty
(5) transplant
(6) delete_fixup() changes colors and performs rotations to restore RB properties

Applications:
(1) efficiement implementation of associate arrays
(2) efficient implementation of priority queue
(3) efficient implementation of dynamic set operations

Vioaltions when insertin ga nod einto RB tree
(1) if root node is being inserted -> new root is black
(2) if the parent node is black -> new node is red
(3) if parent is red node: insert as black node
    - (3a) uncle is red: recolor inserted node and prent to black, grandparent to red, fix violations
    - (3b) uncle is black (or null)
        (LL) if new node is left child, perform righ trotation on grandparent
        (LR) if new node is right child, perform left rotation on parent, right rotation on grandparent
        (RR) if new node right child, perform left rotation on grandparent
        (RL) if new node is left child, perofrm righ toration on praent and lef tortation on grandparent 
'''

from redblacktree import rbtree
tree = rbtree([1,2,(3, 'three'), 4])
tree.insert(4, 'four')
print(tree[3])