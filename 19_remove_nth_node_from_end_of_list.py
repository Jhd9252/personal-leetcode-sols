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
        # the idea is to find the nth node from end of linked list
        # then have a left pointer towards the previous node
        # then have a right pointer towards teh next node
        # and then connect the two nodes, essentially cutting the nth node out
        
        
        # in order to traverse the linked list, we need the length of LL
        # since we must return the head of result, create a pointer var = head
        # the target node is = length of linked list - nth integer
        
        length = 0
        copy = head
        while copy:
            length += 1
            copy = copy.next
        # length - n + 1
        target = length - n   # gets index of node to remove

        # create a pointer for the left node of nth
        left = head
        
        
        # cover cases
        
        # if the nth node to remove is the length of the linked list
        # remove the first node
        if n == length:
            left = left.next
            return left
        
        # if nth node is greater than or equal to 2, move the left node to right before nth node
        # create and move right node two positions from left pointer
        # connect the two, return the head
        elif n >= 2:
            for i in range(target -1 ): 
                left = left.next #at node before nth from last
            right = left
            for i in range(2):
                right = right.next
            left.next = right
            return head
        # if the nth node is the last, and the length of LL is 1, return None
        elif n == 1 and length == 1:
            return None
        
        # if nth node to remove is the last
        # n == 1 and length ==1 is alreay covered
        # so this covers n==1, and length any size except 1 
        # move the left pointer to the second to last node.
        # set left.next = None and return head
        elif n == 1:# else n < 2, which is only 1 or 0
            for i in range(target -1 ): 
                left = left.next #at node before nth from last
            left.next = None
            return head
        
        # covered n>=2 for matching/non matching, n == 1 for matchin/non-matching lengths
        # now if not those, then n==0, simply return head as is. 
        else: 
            return head