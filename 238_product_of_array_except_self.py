# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 10:33:06 2022

@author: jhd9252


Title: 238. Product of Array Except Self


Given an integer array nums, return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in 
a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using 
the division operation.

 


Input: nums = [1,2,3,4]
res: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
res: [0,0,9,0,0]
"""
class Solution:
    def productExceptSelf(self, nums):
        # store result
        res = [1] * len(nums)
        # store length of nums
        n = len(nums)
        # set temp value = 1
        temp=1
        # first pass left to right from index 1 through end
        for i in range(1,n):
            # temp accumulates x*y
            # store the pre fix values in res
            temp=temp*nums[i-1]
            res[i]*=temp
        # reset temp value = 1
        temp=1
        # second pass from right to left, from last idx - 1, to first index
        for i in range(n-2,-1,-1):
            # temp accumulates post fix y*x
            temp=temp*nums[i+1]
            # store the post * pre into res
            res[i]*=temp  
        # runs in O(n) time
        return res
        