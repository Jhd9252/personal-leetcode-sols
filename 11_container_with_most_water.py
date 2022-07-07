# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 16:26:12 2022

@author: jhd9252

title: 11 container with most water

You are given an integer array height of length n. There are n vertical lines 
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the 
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Constraint:
    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
"""

class Solution:
    def maxArea(self, height) -> int:
        
        """
        # brute force for loops
        # time limit exceeded
        res = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area = (j - i) * min(height[i], height[j])
                res = max(res, area)
        return res
        """
        
        # two pointer solution
        # update pointers based on the limiting factors of distance and min(height)
        # since the pointers - > factor of distance
        # then shift pointers based on min(height)
        # O(n) running time complexity
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                # else left > right, or l == r. 
                r -= 1
        return res
        
