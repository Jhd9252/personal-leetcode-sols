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
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Brute Force: Take all values, sort, create new LL
        Runtime: O((n+m) log (n+m))
        Space: O(n+m)
        '''
        arr = []
        while list1:
            arr.append(list1.val)
            list1 = list1.next 
        while list2:
            arr.append(list2.val)
            list2 = list2.next

        arr.sort()
        dummy = ListNode()
        ptr = dummy
        for num in arr:
            newNode = ListNode(num)
            ptr.next = newNode
            ptr = ptr.next
        return dummy.next 

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Two Pointer Method - In Place
        Note: Keep the pointers ahead of the current 
        Time: O(m+n)
        Space: O(1)
        """
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next 
            else:
                curr.next = list2
                list2 = list2.next 
            curr = curr.next 
        curr.next = list1 or list2 
        return dummy.next 

        