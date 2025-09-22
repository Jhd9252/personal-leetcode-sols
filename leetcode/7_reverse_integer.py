
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:25:19 2022

@author: jhd9252

LeetCode Problem: 7. Reverse Integer
Test Cases: 1032 / 1032 test cases passed.
Runtime: 46 ms (beats 53.35 % of python3 submissions)
Memory Usage: 13.9 MB (beats 68.05 % of python3 submissions)

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


Constraints:
    -231 <= x <= 231 - 1
"""

class Solution:
    def reverse(self, x: int) -> int:
        y = int(str(abs(x))[::-1])
        if x < 0:
            y = 0 - y
        if y not in range((-2)**31, 2**31):
            return 0
        else:
            return y