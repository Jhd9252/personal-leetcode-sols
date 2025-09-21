# -*- coding: utf-8 -*-
"""
Created on Tues Apr 12 19:25:19 2022

@author: jhd9252

LeetCode Problem: 24. Swap Nodes in Pairs
Test Cases: 55 / 55 test cases passed.
Runtime: 32 ms, faster than 89.06% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 13.9 MB, less than 67.76% of Python3 online submissions for Swap Nodes in Pairs.


You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Constraints:
    k == lists.length
    0 <= k <= 104
    0 <= lists[i].length <= 500
    -104 <= lists[i][j] <= 104
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 104.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # if the head exists, as in there is a valid input
        if head:                                          
            # set dummy node = head.next
            next_pos = head.next               
            # if the second node exists and is valid
            if next_pos:
                # connect pos2 -> pos1, connect pos1 to pos3
                next_pos.next, head.next = head, next_pos.next           
                # recursion starting at pos3
                next_pos.next.next = self.swapPairs(next_pos.next.next)  
                return next_pos
        # else if no valid input, return 
        return head                   
        