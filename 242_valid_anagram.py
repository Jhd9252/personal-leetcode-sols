# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 16:47:25 2022

@author: jhd9252

Title: 242 valid anagram
Test Cases: 
Runtime: 93 ms, faster than 24.74% of Python3 online submissions for Valid Anagram.
Memory Usage: 15.4 MB, less than 11.50% of Python3 online submissions for Valid Anagram.


Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.

"""
class Solution:
    def isAnagram(self, s,t):
        if len(s) != len(t):
            return False
        l1 = sorted([x for x in s])
        l2 = sorted([x for x in t])
        return l1 == l2
        
        
    

        