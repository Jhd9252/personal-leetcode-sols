# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        M1: Get an array, create left pointer (0), right pointer (n-1)
        M2: Find the middle of the LL, reverse from mid->end, merge
        runtime: O(n)
        space: O(1)
        """
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        # reverse from slow onwards
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # prev is head of reversed list
        while head and prev:
            tmp = head.next
            head.next = prev
            head = tmp

            tmp = prev.next
            prev.next = head 
            prev = tmp
        
        if head:
            head.next = prev
        else:
            prev.next = head
    
