# -*- coding: utf-8 -*-
"""
Created on Tues Apr 12 19:25:19 2022

@author: jhd9252

LeetCode Problem: 9. Palindrome Number
Test Cases: 55 / 55 test cases passed.
Runtime: 64 ms, faster than 85.93% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.8 MB, less than 63.82% of Python3 online submissions for Palindrome Number.


Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Constraints:
    k == lists.length
    0 <= k <= 104
    0 <= lists[i].length <= 500
    -104 <= lists[i][j] <= 104
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 104.
"""




class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr = [x for x in str(x)]
        if len(arr) % 2 == 0:
            return arr[0: int(len(arr) /2)] == arr[-1:int(len(arr)/2)-1:-1]
        else:
            return arr[:int(len(arr)/2)] == arr[-1:int(len(arr)/2):-1]

alpha = Solution()
bravo = alpha.isPalindrome(12321)
print(bravo)
        
         