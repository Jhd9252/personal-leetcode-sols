
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
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        Naive: Merge and sort in an extra array
        RT: O(nlogn)
        Space: O(n+m)
        '''
        merged = sorted(nums1 + nums2)
        # odd length
        if len(merged) % 2:
            return merged[len(merged) // 2]
        # even length
        else:
            return (merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2
        
        merged = sorted(nums1 + nums2)
  
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        Merge arays with two pointer walk through
        RT: O(n+m)
        Space: O(n+m)
        '''
        merged = []
        left, right = 0, 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                merged.append(nums1[left])
                left += 1
            else:
                merged.append(nums2[right])
                right += 1
        merged += nums1[left:] or nums2[right:]
        if len(merged) % 2:
            return merged[len(merged) // 2]
        else:
            return (merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        Both arrays are sorted in increasing order. 
        We know both lengths, can determine odd or even, and median in O(1) time. 
        Partition arrays such that both left portions are < both right portions. 
        To get O(logn(n+m)) then we konw that binary division, 
        Take overall half - current first pointer. 
        (1) ensure minimum of both sides less than other side
        (2) ensure maximum of both sides are greater than. 
        (3) Ensure edge case when full array is partitioned
        '''
        A, B = nums1, nums2 
        length = len(nums1) + len(nums2)
        half = length // 2
        if len(B) < len(A):
            A, B = B, A

        
        left, right = 0, len(A) - 1

        while True:
            # set our mids, mins, max
            a_mid = (left + right) // 2
            b_mid = length - a_mid - 2 # minus for two arrays in 0-index

            # get current boundaries
            a_max = A[a_mid] if a_mid >= 0 else float('-inf')
            a_min = A[a_mid + 1] if a_mid + 1 < len(A) else float('inf')

            b_max = B[b_mid] if b_mid >= 0 else float('-inf')
            b_min = B[b_mid + 1] if b_mid + 1 < len(B) else float('inf')

            # if boundaries are good, it is a valid partition
            if a_max <= b_min and b_max <= a_min:
                # if odd length
                if length % 2:
                    return min(a_min, b_min)
                else:
                    return max((a_max, b_max) + min(a_min, b_min)) / 2
            else:
                if b_max > a_min:
                    left = a_mid + 1
                else:
                    right = a_mid - 1

