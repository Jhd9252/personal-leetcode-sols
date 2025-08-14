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

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Brute Force : Two for loops (i, j=i+1)
        Runtime: O(n**2)
        Space: O(1) 
        '''
        n = len(numbers)
        for i in range(n):
            for j in range(i+1, n):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Binary Search
        Runtime: O(nlogn) 
        Space: O(1) 
        '''

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Hashmap : {num : idx}
        Runtime: O(n)
        Space: O(n)
        '''
        seen = {}
        for idx, num in enumerate(numbers):
            left = target - num 
            if left in seen:
                return [seen[left] + 1, idx + 1]
            seen[num] = idx 
            
    def twoSum(self, numbers:List[int], target:int) -> List[int]:
        '''
        Two Pointer Approach: Shift according to sum ? target 
        Runtime: O(n)
        Space: O(1) 
        '''    
        l, r, = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1


