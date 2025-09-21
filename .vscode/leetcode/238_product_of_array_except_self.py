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
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Brute Force: Two for loops (outer = placement in answer array, inner = iterate through product array)
        RT: O(n**2)
        Space: O(1) 
        '''
        answer = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    answer[i] *= nums[j]
        return answer

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Using Pre and Post fix arrays 
        RT: O(3n) = O(n)
        Space: O(3n) = O(n)
        '''
        n = len(nums)
        pre = [1] * n 
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]
        
        post = [1] * n
        for i in range(n-2, -1, -1):
            post[i] = post[i+1] * nums[i+1]

        answer = [1]*n
        for i in range(n):
            answer[i] = pre[i] * post[i]

        return answer

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Running Pre and Post Fix products
        RT: O(2n) = O(n)
        Space: O(n)
        '''
        if not nums: return []
        pre, post = 1, 1 

        answer = [1] * len(nums)
        for i in range(len(nums)):
            answer[i] *= pre
            pre *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= post
            post *= nums[i]
        return answer

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Single Pass with running pre and post sums
        RT: O(n)
        Space: O(n)
        '''
        if not nums: return []
        pre, post = 1, 1
        answer = [1] * len(nums)
        for i in range(len(nums)):
            answer[i] *= pre
            pre *= nums[i]
            answer[len(nums) - 1 - i] *= post
            post *= nums[len(nums) -1 - i]
        return answer

  