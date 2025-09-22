# -*- coding: utf-8 -*-
"""

Title: 128 longest consecutive sequence (not ordered)

Given unsorted array of integers, return length of longest
consecutive elements sequence. Must be O(n) time. 

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # exceptions
        if len(nums) == 1: return 1
        if len(nums) == 0: return 0

        # initialize 
        best = 0
        nums = set(nums)

        # check each number if it is a starting point
        for x in nums:
            if (x-1) not in nums:
                # if it is, then starting at length 1
                length = 1
                # while the next num exists, increment
                while (x + length) in nums:
                    length += 1
                # after end point, compare
                best = max(best, length)
        # return result 
        return best
