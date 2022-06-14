# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 18:20:05 2022

@author: jhd9252


Problem: 5. Longest Palindromic String

Given a string, s, return the longest palindromic substring in s.

Constraints:
    1 <= s.length <= 1000
    s consists of only digits and English letters


Implementation:
    Recursive center expansion algorithm
    Starting with first letter
    For i in length of string
    With helper function, return the slice thats longest palindrome
    with each loop, compare and get max length of substring
"""



class Solution:
    def longestPalindrome(self, s: str) -> str:
        # holder variable
        res = ''
        # for loop len(s)
        for i in range(len(s)):
            # holder variable for palindrome (string, left, right + 1)
            # this case is for possible even length strings
            res1 = self.get_palindrome(s, i, i+1)
            # holder variable for palinfrome (string, left, right)
            # this case is for possible odd length palindromes
            res2 = self.get_palindrome(s, i, i)
            # compare the palindromes, and obtain the longest
            res = max([res, res1, res2], key=lambda x: len(x))
        # return the result
        return res
    
    # helper function
    # while the left pointer is in range, and the right pointer in range, and l=r
    # move the pointers outwards
    # return the longest palindrome from that implicit center
    def get_palindrome(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]