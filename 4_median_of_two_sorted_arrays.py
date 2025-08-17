
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
        naive: merge and sort in extra array
        rt: O(nlogn)
        space: O(n+m)
        '''
        merged = sorted(nums1 + nums2)
        if len(merged) % 2:
            return merged[len(merged) // 2]
        else:
            return (merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        Merge arrays through a two pointer walk
        RT: O(n + m)
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
            return (merged[len(merged) // 2] + merged[len(merged) // 2 -1]) / 2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        Both arrays are sorted in non-descending order. 
        If we know the length of nums1 + nums2, and determine even/odd, we can calculate median in O(1) time. 
        How do we partition both arrays, in two left parts, and two right parts, that virtualize a single array. 
        We know that O(log(n+m)) implicitly points to binary search. So, using one array, find a median or middle.
        We can simulate O(log (n+m)) by taking away half from length(nums1 + nums2).
        So find a median in one array, take half (rounded) down, subtract from size of left array including median. 
        The size of the other left array is half - current left. 
        To check if our two paritions simualte a single array, we need that
        (1) minimum of both sides, is less than the other side
        (2) the max of both left paritions, are less than the other in of other parition. 
        Keep in mind what happens when a full array is paritioned. 
        '''
        A, B = nums1, nums2
        length = len(nums1) + len(nums2)
        half = length // 2
        if len(B) < len(A):
            A, B = B, A

        left, right = 0, len(A) - 1
        while True: # return when we find our correct partition
            a_mid = (left + right) // 2 
            b_mid = half - a_mid - 2 # two arrays that are 0-index

            a_max = A[a_mid] if a_mid >= 0 else float('-inf') # if the entire partition is on the other array, make A max = -inf, so pass check
            a_min = A[a_mid + 1] if a_mid + 1 < len(A) else float('inf') # If there is no right parition, then we want to pass check 
            b_max = B[b_mid] if b_mid >= 0 else float('-inf')
            b_min = B[b_mid + 1] if b_mid + 1 < len(B) else float('inf')

            if a_max <= b_min and b_max <= a_min:
                if length % 2:
                    return min(a_min, b_min)
                else:
                    return (max(a_max, b_max) + min(a_min, b_min)) / 2
            else:
                if b_max > a_min:
                    left = a_mid + 1
                else:
                    right = a_mid - 1

 
            
            
            
        