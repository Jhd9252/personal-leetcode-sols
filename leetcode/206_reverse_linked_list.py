# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ''' Iterative Approach '''
        if not head:
            return None
        prev, curr = None, head
        while curr:
            nxt = curr.next 
            curr.next = prev
            prev = curr 
            curr = nxt 
        return prev 

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ''' Recursive Approach '''
        # base case
        if not head or not head.next:
            return head 

        # post process

        # get res from below
        nHead = self.reverseList(head.next)

        # assign next's next back toward current node
        head.next.next = head
        # get rid of this node's next 
        head.next = None 
        # return this node upwards to repeat
        return nHead