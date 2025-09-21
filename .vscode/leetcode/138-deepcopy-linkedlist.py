"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ''' 
        Deep Copy
        Problem: We need a method to create a node and hold off on attribute assignment. 
        Intuition: 
            - Create a mapper {real : copy} such that initially, nodes have None attributes.
            - We then iterate through every real node, get copy node, and reassign.
            - Make sure to account for NULL next pointers and random pointers. 
            - Either make mapper values NULL by default, or use the get(key, or) method. 
        Runtime: O(n)
        Space: O(n)
        '''
        mapper = collections.defaultdict(lambda: Node(0))
        mapper[None] = None
        curr = head
        while curr:
            mapper[curr].val = curr.val
            mapper[curr].next = mapper[curr.next]
            mapper[curr].random = mapper[curr.random]
            curr = curr.next 
        return mapper[head]

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapper = {} # { real : copy}
        dummy = head
        curr = dummy
        while head:
            mapper[head] = Node(head.val)
            head = head.next
        while curr:
            mapper[curr].next = mapper.get(curr.next, None)
            mapper[curr].random = mapper.get(curr.random, None)
            curr = curr.next
        return mapper.get(dummy, None)
        
        




        