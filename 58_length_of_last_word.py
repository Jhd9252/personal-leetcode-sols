# -*- coding: utf-8 -*-
"""
Created on Tues Apr 12 19:25:19 2022

@author: jhd9252

LeetCode Problem: 58. Length of Last Word
Test Cases: 113 / 113 test cases passed.
Runtime:  41 ms, faster than 56.68% of Python3 online submissions for Length of Last Word.
Memory Usage: 13.8 MB, less than 83.26% of Python3 online submissions for Length of Last Word.


Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
 

Constraints:
    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.
"""


def lengthOfLastWord(s):
    s = s.lstrip()
    s = s.rstrip()
    return len(s.split(' ')[-1])

print(lengthOfLastWord("   fly me   to   the moon  "))