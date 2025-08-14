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
    def maxArea(self, height: List[int]) -> int:
        '''
        Brute Force with two for loops
        RT: O(n**2)
        Space: O(1)
        '''
        res = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                res = max(res, min(height[i], height[j]) * (j - i))
        return res 

    def maxArea(self, height: list[int]) -> int:
        '''
        Two Pointer :
        (1) maxArea is theoretically : MAXLENGTH * MAX(MIN(LEFT, RIGHT))
        (2) Starting at the ends gives us MAXLENGTH
        (3) Shift pointers inward trying to max the min of left and right
        RT: O(n)
        Space: O(1) 
        '''
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            res = max(res, min(height[l], height[r]) * (r-l))
            if height[l] < height[r]: l += 1
            else: r -=1 
        return res 
        
