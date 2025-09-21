# -*- coding: utf-8 -*-
"""
LeetCode Problem: 88. Merge Sorted Array
TestCases: 59 / 59 test cases passed.
Runtime: 54 ms
Memory Usage: 13.9 MB

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
 and two integers m and n, representing the number of elements in nums1 and nums2 
 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be 
stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged, and the 
last n elements are set to 0 and should be ignored. nums2 has a length of n.

Constraints:
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[j] <= 109
    

Given 2 integer arrays in non-decreasing order
Given m is elements of num1s array
Given length of nums1 is m + n, with the n-elements being zeroes
Given n is elements of nums2 array

Merge the two arrays in-place (nums1)
Do not return anything
"""

def func(nums1, m, nums2, n):
    # start the merge at the end of the lists
    # grab the last index of each nums1, nums2 as pointers
    p1, p2 = m - 1, n - 1
    
    # for destination index of merged array, working backwards
    # this works because the constraints given 
    for i in range(m + n - 1, -1, -1):
        
        # if second list is empty, nothing more to merge, return to end
        if p2 < 0:
            return
        
        # if nums1 p1 has not reached the beginning
        # compare and insert at destination i
        if p1 >= 0 and nums1[p1] > nums2[p2]:                
            nums1[i] = nums1[p1]
            p1 -= 1
        else:
            nums1[i] = nums2[p2]
            p2 -= 1

