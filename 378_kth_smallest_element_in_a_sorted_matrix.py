# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:25:19 2022

@author: jhd9252

LeetCode Problem: 378. Kth Smallest Element in a Sorted Matrix
Test Cases: 86/86 passed
Runtime: 239 ms (beats 68.02% of python3 submissions)
Memory Usage: 13.8 MB (beats 83.81% of python3 submissions)


Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

Constraints:
    n == matrix.length == matrix[i].length
    1 <= n <= 300
    -109 <= matrix[i][j] <= 109
    All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
    1 <= k <= n2
"""

class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        a = []
        for sub in matrix:
            for i in sub:
                a.append(i)
        return sorted(a)[k-1]