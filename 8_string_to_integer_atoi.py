
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:25:19 2022

@author: jhd9252

LeetCode Problem: 8. String to Integer (atoi)
Test Cases: 1082 / 1082 test cases passed.
Runtime: 46 ms (beats 62.21 % of python3 submissions)
Memory Usage: 14 MB 

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.


Constraints:
    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
    0 <= s.length <= 200
    s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        # clean string
        s = s.lstrip()
        s = s.rstrip()
        mylist = []
        
        pos = True
        signed = False
        
        for char in s:
            if signed:
                if char.isnumeric():
                    mylist.append(char)
                elif (char.isnumeric() == False):
                    break
            else:
                if char == '+':
                    pos = True
                    signed = True
                elif char == '-':
                    pos = False
                    signed = True
                elif char.isnumeric():
                    signed = True
                    mylist.append(char)
                else:
                    break
                    
        if len(mylist) == 0:
            return 0
    
        result = int(''.join(mylist))
        
        if pos == False:
            result = 0- result
        
        if result < -2147483648:
            return -2147483648
        elif result > 2147483647:
            return 2147483647
        else:
            return result