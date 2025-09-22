# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:21:37 2022

@author: jhd9252


LeetCode Problem: 1523 Count Odd Numbers in an Interval Range
Test Cases: 84/84 passed
Runtime: 35 ms (beats 10.4% of python submissions)
Memory Usage: 13.8 MB 


Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

Constraints:
   0 <= low <= high <= 10^9
"""


class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        div = (high-low) // 2
        if (high%2 != 0) or (low%2!=0):
            div +=1
        return div
            
        