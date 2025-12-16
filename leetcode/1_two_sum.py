# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:25:19 2022

@author: jhd9252

LeetCode Problem: 1. Two Sum
Test Cases: 57/57 passed
Runtime: 8892 ms 
Memory Usage: 15 MB (beats 77.6% of python3 submissions)


Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Constraints:
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ''' Brute Force, RT O(n^2), Space O(1)'''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [None, None]
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        Optimized with HashMap for O(1) lookup time
        RT: O(n)
        Space: O(n)
        '''
        seen = {} # number, index
        for i, v in enumerate(nums):
            leftover = target - v
            if leftover in seen:
                return [seen[leftover], i]
            seen[v] = i
        return [None, None]
        