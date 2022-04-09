# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:25:19 2022

@author: jhd9252

LeetCode Problem: 21 Merge Two Sorted Lists
Test Cases: 208 / 208 test cases passed.
Runtime: 64 ms (runtime beats 26.72 % of python3 submissions.)
Memory Usage: 13.9 MB (memory usage beats 36.02 % of python3 submissions.)

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next         
    
class Solution:
    def mergeTwoLists(self, list1, list2):
        # both LL are sorted in ascending order
        # compare both current nodes a, b
        # connect the lesser to greater
        # move the lesser to up the chain
        # if current a or b node is null, connect the rest
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        result = ListNode(0)
        current = result
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.val = list1.val                
                list1 = list1.next
            else:
                current.val = list2.val                
                list2 = list2.next
            if list1 and list2:                
                current.next = ListNode(0)
                current = current.next
            else:
                break
            
        if list1 == None:
            current.next = list2
        elif list2 == None:
            current.next = list1
        return result

        