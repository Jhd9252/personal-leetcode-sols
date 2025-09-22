# -*- coding: utf-8 -*-
"""
Created on Tues Apr 12 19:25:19 2022

@author: jhd9252

LeetCode Problem: 23. merge k sorted linked lists
Test Cases: 133 / 133 test cases passed
Runtime: 103 ms, faster than 92.45% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 18.5 MB, less than 20.85% of Python3 online submissions for Merge k Sorted Lists.


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
   
    def mergeKLists(self, lists):
        arr = []
        if len(lists) == 0:
            return None
        
        for l in lists:
            while l:
                arr.append(l.val)
                l = l.next
        if len(arr) == 0:
            return None
        arr = sorted(arr)
        head = ListNode(arr[0])
        copy = head
        for i in range(1, len(arr)):
            copy.next = ListNode(arr[i])
            copy = copy.next
        return head