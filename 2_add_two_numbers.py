
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

    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ''' Brute Force Naive: Get the ints, reverse, add, create new linked list '''
        pass

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        Two Pointers:
        '''
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ''' 
        Less verbose 
        RT: O(n+m)
        Space: O(1)
        '''
        dummy = cur = ListNode(0)           # create dummy node to return, curr to move
        carry = 0                           # this is the carry for addition
        while l1 or l2 or carry:            # while there is still something to add
            if l1:                          # if l1 exists, add its value to carry 
                carry += l1.val
                l1 = l1.next
            if l2:                          # if l2 exists, add its value to carry   
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)   # creates a node with leftover after mod 10
            cur = cur.next
            carry //= 10                    # set carry to be 0 or 1 depending on div 10
        return dummy.next
                
            