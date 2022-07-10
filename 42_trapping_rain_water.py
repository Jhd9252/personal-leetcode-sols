# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 18:03:46 2022

@author: jhd9252

Title: 42_trapping_rain_water

Given, n, non-negative integers representing an elevation map where the 
width of each bar is 1, compute how much water it can trap after raining. 

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by 
array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
are being trapped.

Constraints:
    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105
"""

class Solution:
    def trap(self, height):
        # We want to count the amount of water each index can holds
        # Except the first and last index, can't hold water
        # Each index, we find the left_max and right_max.
        # The minimum of left_max and right_max minus the value of current index
        # determines the amount of water being held at that index
        # The first and last index has left_max/right_max of zero
        
        """
        # O(n) extra linear memory solution
        # using arrays
        # time limit exceeded
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        minVal = [0] * len(height)
        res = 0
        for l in range(len(height)):
            left_max[l] = max(height[:l], default = 0)
        for r in range(len(height)):
            right_max[r] = max(reversed(height[r+1:]), default = 0)
        for i in range(len(height)):
            res += max(0, min(left_max[i], right_max[i]) - height[i])
        return res
        
        # using 1 pass
        # time limit exceeded
        res = 0
        for i in range(len(height)):
            left_max = max(height[:i], default = 0)
            right_max = max(height[i+1:], default = 0)
            res += max(min(left_max, right_max) - height[i],0)
        return res
        """
        
        # using pointers
        # initializing pointers and vars from lmax and rmax
        # shift a pointer according to which is smaller/equal
        # the variable corresponding to shift is smaller, and therefore we now the min (left, right)
        # think of this as a condition for using pointers, and cutting running time
      
        # special case
        if not height:
            return 0
        
        l, r = 0, len(height) -1
        lmax, rmax = height[l], height[r]
        res = 0
        
        while l < r:
            if lmax < rmax:
                l+=1
                lmax = max(lmax, height[l])
                res += lmax - height[l] # will never be negative, because we update max(0, var) beforehand
            else:
                r -= 1
                rmax = max(rmax, height[r]) 
                res += rmax-height[r]
        return res
        
        
        
        
    
    
height = [0,1,0,2,1,0,1,3,2,1,2,1]     
a = Solution()
b = a.trap(height)