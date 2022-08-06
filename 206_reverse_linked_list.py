
206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head, prev = None):
        # set the pointers prev (left) and curr (mid)
        prev = None
        curr = head

        # while curr is a valid node
        while curr:
            # set next = curr.next (right) pointer
            next = curr.next         

            # exchange connections
            curr.next = prev
            prev = curr
            curr = next

        return prev
