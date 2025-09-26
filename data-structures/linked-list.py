class Node: 
    def __init__(self, val, prev = None, nxt = None):
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LinkedList:
    def __init__(self):
        self.head = Node(0)

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
            return 
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)
    
    def insert(self, data, pos):
        if not self.head or pos == 1:
            nNode = Node(data)
            nNode.next = self.head
            self.head = nNode
            return 
        p = 1
        prev, curr = None, self.head
        while curr and p < pos:
            prev, curr = curr, curr.next
        if not curr: return None
        prev.next = Node(data)
        prev.next.next = curr


    def delete(self, data):
        if not self.head: return None
        prev, curr = None, self.head
        while curr and curr.val != data:
            prev, curr = curr, curr.next
        if curr.val != data: return None
        prev.next = curr.next
        curr.next = None

    def delete(self, pos):
        if not pos or not self.head: return None
        if pos == 1: self.head = None
        p = 1
        prev, curr = None, self.head
        while curr and p < pos:
            prev, curr = curr, curr.next
        if curr is None: return None
        prev.next = curr.next
        curr.next = None
        return 
    
    def search(self, data):
        if not self.head: return -1
        curr = self.head
        while curr and curr.val != data:
            curr = curr.next
        if not curr: return -1
        return curr


    def detect_cycle(self):
        if not self.head or not self.head.next: return False
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False 

    def start_cycle(self):
        if not self.detect_cycle(): return None

        slow, fast = self.head, self.head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        slow = self.head
        while slow and fast:
            slow, fast = slow.next, fast.next
            if slow == fast:
                return slow


