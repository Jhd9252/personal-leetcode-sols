# -*- coding: utf-8 -*-
"""
Created on Tues Apr 12 19:25:19 2022

@author: jhd9252

LeetCode Problem: 27. Remove Element
Test Cases: 113 / 113 test cases passed.
Runtime:  35 ms, faster than 86.34% of Python3 online submissions for Remove Element..
Memory Usage: 13.8 MB, less than 67.05% of Python3 online submissions for Remove Element.


Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
 

Constraints:
   0 <= nums.length <= 100
    0 <= nums[i] <= 50
    0 <= val <= 100
"""


class Solution:
    def removeElement(self, nums, val, pos = 0):
        # base case of position reaching end of integer array
        if pos == len(nums) - 1:
            if nums[pos] == val:
                del nums[pos]
                return len(nums)
            else:
                return len(nums)
        # base case /edge case of len(nums) == 0
        elif len(nums) == 0:
            return 0
        else:
            if nums[pos] == val:
                del nums[pos]
                return self.removeElement(nums, val, pos)
            else:
                return self.removeElement(nums, val , pos + 1)
        
        
        