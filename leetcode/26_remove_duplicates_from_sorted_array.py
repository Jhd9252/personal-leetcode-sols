"""
Created on Fri Apr  8 19:25:19 2022

@author: jhd9252

LeetCode Problem: 26. Remove Duplicates from Sorted Array
Test Cases: 361 / 361 test cases passed.
Runtime: 314 ms (runtime beats 6.05 % of python3 submissions.)
Memory Usage: 15.5 MB ( memory usage beats 65.50 % of python3 submissions.)

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Constraints:
    1 <= nums.length <= 3 * 104
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.
"""

# given array sorted in acsending order, remove duplicates in place
# return k length of arr, with modified arr

class Solution:
    # option 1
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 1:
            return 1   
        i = 1
        while i in range(1,len(nums)):
            if nums[i] == nums[i-1]:              
                del nums[i]
            else:
                i += 1        
        return len(nums)
    
    """
    def removeDuplicates(self, nums):
        i = 0
        while i in range(len(nums)):
            if nums.count(nums[i]) > 1:
                del nums[i]
            else:
                i += 1
        return len(nums)
    """