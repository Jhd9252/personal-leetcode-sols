# -*- coding: utf-8 -*-
"""
Created on Tues Apr 12 19:25:19 2022

@author: jhd9252

LeetCode Problem: 15. 19. Remove Nth Node From End of List
Test Cases: 208 / 208 test cases passed.
Runtime:  Runtime: 36 ms ( runtime beats 84.94 % of python3 submissions)
Memory Usage: 13.9 MB (74.12 % of python3 submissions.)


Given the head of a linked list, remove the nth node from the end of the list and return its head.
Constraints:
  The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ''' Use two pointers with a range of n -> move to end of list '''
        # initialize our two pointers and stagger them
        slow, fast = head, head
        for i in range(n):
            fast = fast.next

        # find an edge case where n == length of list
        # then the node to delete is the first node
        if not fast: return head.next

        # edge case where if fast is last node, and node to delete is last
        # move until we reach last node, thus we have prev
        while fast.next:
            slow, fast = slow.next, fast.next
        
        # set slow next to skip
        slow.next = slow.next.next
        return head