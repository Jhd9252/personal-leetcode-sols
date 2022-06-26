# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 16:47:25 2022

@author: jhd9252

Title: Contains Duplicate
Test Cases
Memory:  25.9 MB, less than 71.84% of Python3 online submissions for Contains Duplicate.
Running Time: 769 ms, faster than 24.40% of Python3 online submissions for Contains Duplicate.


Given an integer array 'nums', return True if any value appears at least twice
in the array. Return False if every every element is distinct.


"""



class Solution:
    def containsDuplicate(self, nums):
        # O(n) running time.
        # with n being the second occurence or end of array. 
        h = set()
        for n in nums:
            if n in h:
                return True
            h.add(n)
        return False
    