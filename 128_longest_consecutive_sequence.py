# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 19:30:14 2022

@author: jhd9252

Title: 128 longest consecutive sequence (not ordered)

Given unsorted array of integers, return length of longest
consecutive elements sequence. Must be O(n) time. 

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

# Most sorting algorithms are O(nlogn)
class Solution:
    def longestConsecutive(self, nums):
        # base case
        if len(nums) == 0:
            return 0
        # base case
        if len(nums) == 1:
            return 1
        # Since we are counting CONSECUTIVE elements, we can get rid of repeats by converting to set
        res, s = 0, set(nums)
        for num in nums:
            if (num-1) not in s: # then current num is the start of a sequence
                l = 1
                while (num + l) in s:
                    l += 1
                res = max(res, l)
        return l
        