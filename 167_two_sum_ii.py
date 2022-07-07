# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 20:14:50 2022

@author: jhd9252

167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Constraints:
    2 <= numbers.length <= 3 * 104
    -1000 <= numbers[i] <= 1000
    numbers is sorted in non-decreasing order.
    -1000 <= target <= 1000
    The tests are generated such that there is exactly one solution.
    
Purpose: Two pointers
"""

# input: numbers array, integer target
# process: find the 2 indexes that add to target
#   left pointer starts at index 0
#   right pointer starts at index len(numbers) -1
#   the array sorted in increasing order
#   as long as p1 + p2 < target, move left pointer
#   as long as p1 + p2 > target, move right pointer
# output: array length 2, of index + 1
class Solution:
    def twoSum(self, numbers, target):
        # two pointer solution
        p1, p2 = 0, len(numbers) - 1
        while p1 < p2:
            t = numbers[p1] + numbers[p2]
            if t == target: 
                return [p1+1, p2+1]
            elif t < target:
                p1 += 1
            else:
                p2 -= 1
                
                
        
                

