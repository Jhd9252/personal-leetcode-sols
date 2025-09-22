# -*- coding: utf-8 -*-
"""
242. Valid Anagram
Difficulty: easy

Problem: Given two strings s and t, return true if t is an anagram of s and false otherwise.

"""
from matplotlib import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Sort the strings and compare with pointers
        RT: O(n log n)
        Space: O(s+t)
        '''
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
    
    def isAnagram2(self, s: str, t: str) -> bool:
        '''
        Brute Force Naive: Two hashmaps
        RT: O(s + t + (s+t)) = O(s+t)
        Space: O(1) for 2*26 fixed hashmaps
        '''
        if len(s) != len(t):
            return False
        counter1 = collections.Counter(s)
        counter2 = collections.Counter(t)
        return counter1 == counter2
    
    def isAnagram3(self, s: str, t: str) -> bool:
        '''
        Memory Optimization with Single Hashmap
        RT: O(s+t)
        Space: O(1) for 26 fixed hashmaps
        '''
        if len(s) != len(t):
            return False
        counter = collections.Counter(s)
        for c in t:
            if c not in counter or counter[c] == 0:
                return False
            counter[c] -= 1
        return True
