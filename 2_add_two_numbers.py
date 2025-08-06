
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:25:19 2022

@author: jhd9252

LeetCode Problem: 2. Add Two Numbers
Test Cases: 1568 / 1568 passed
Runtime: 136 ms (beats 11.8% of python3 submissions)
Memory Usage:  14 MB (beats 47.23% of python3 submissions)

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Naive: Track numbers, reverse, create new LL
        """
        num1 = []
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        num2 = []
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        num3 = str(int(''.join(map(str,num1[::-1]))) + int(''.join(map(str,num2[::-1]))))
        dummy = ListNode()
        curr = dummy
        for char in num3[::-1]:
            curr.next = ListNode(int(char))
            curr = curr.next
        return dummy.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Two Pointer Solution with CarryOver
        """
        if not l1 and not l2: return ListNode()
        elif not l1: return l2
        elif not l2: return l1
    
        p1, p2 = l1, l2
        dummy = ListNode()
        head = dummy
        carry = False
        while p1 and p2:
            val = p1.val + p2.val if not carry else p1.val + p2.val + 1
            if val >= 10:
                val %= 10
                carry = True
            else:
                carry = False
            dummy.next = ListNode(val)
            dummy = dummy.next
            p1, p2 = p1.next, p2.next
        
        if not p1:
            while p2:
                val = p2.val if not carry else p2.val + 1
                if val >= 10:
                    val %= 10
                    carry = True
                else:
                    carry = False
                dummy.next = ListNode(val)
                dummy = dummy.next
                p2 = p2.next
        if not p2:
            while p1:
                val = p1.val if not carry else p1.val + 1
                if val >= 10:
                    carry = True
                    val %= 10
                else:
                    carry = False
                dummy.next = ListNode(val)
                dummy = dummy.next
                p1 = p1.next
        if carry:
            dummy.next = ListNode(1)
            dummy = dummy.next
        return head.next
