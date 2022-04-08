
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:25:19 2022

@author: jhd9252

LeetCode Problem: 2. Add Two Numbers
Test Cases: 1568 / 1568 passed
Runtime: 136 ms (beats 11.8% of python3 submissions)
Memory Usage:  14 MB (beats 47.23% of python3 submissions)

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        a = []
        b = []
        while l1:
            a.insert(0,l1.val)
            l1 = l1.next
        while l2:
            b.insert(0,l2.val)
            l2 = l2.next
        result = (str(int(''.join(map(str,a))) + int(''.join(map(str,b)))))
        result = list(result[::-1])
        c = ListNode(0)
        d = c
        while result:
            d.val = int(result[0])
            del result[0]
            if result == []:
                break
            d.next = ListNode(0)
            d = d.next
        return c