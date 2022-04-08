
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:25:19 2022

@author: jhd9252

LeetCode Problem: 4. Median of Two Sorted Arrays
Test Cases: 2094 / 2094 test cases passed.
Runtime:96 ms (beats 90.54% of python3 submissions)
Memory Usage:  14.2 MB (beats 28.75% of python3 submissions)

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Constraints:
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        total = sorted(nums1+nums2)
        i = len(total) // 2
        if len(total) % 2 == 1:
            return total[i]
        else:
            return (total[i-1] + total[i]) /2
        