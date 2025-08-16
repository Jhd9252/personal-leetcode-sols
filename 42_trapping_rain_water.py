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

    '''
    Approach: Pre-compute leftMax and rightMax for each index
    Steps:
        1. Pre-compute leftMax and rightMax for each index
        2. Iterate through each index and calculate water trapped
        water[i] = min(leftMax[i], rightMax[i]) - height[i]
        3. Sum up water trapped for each index
    Time: O(n)
    Space: O(n)
    '''
    from typing import List
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        left = [0] * n
        right= [0] * n
        res = 0 

        for i in range(1, n):
            left[i] = max(left[i-1], height[i-1])

        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i+1])

        for i in range(n):
            res += max(min(left[i], right[i]) - height[i],0)

        return res

    
    '''
    Approach: Two Pointer Approach with running maxes
    Steps:
        1. Initialize two pointers, left and right, at the start and end of the array
        2. Initialize two variables, maxL and maxR, to keep track of the maximum height
        encountered from the left and right respectively
        3. While left < right: move the pointer with the smaller max height 
        4. Update the max height for that pointer
        5. Calculate the water trapped at that pointer and add it to the result
    Note: 
        1. The two pointers are where we calculate volume.
        2. maxL and maxR are running maxes of left and right, and will only increase or stay the same.
        3. If left or right moves and the max is updated, then no water is trapped at that index.
        4. If a max is less than the other max, then we don't need to check the other side, because the min height is the limiting factor.
    Time: O(n)
    Space: O(n)
    '''


    def trap(self, height: list[int]) -> int:
        '''
        Intuition states that runtime of O(n) is our best.
        Is there a way to reduce space?
        Two pointer approach with running maxes. 
        '''
        if not height: return 0

        # left and right pointers are where we calculate volume
        l, r= 0, len(height) - 1

        # maxL and maxR are the current max of left and right
        maxL, maxR = height[0], height[-1]

        res = 0

        # We move left & right according to the maxL & maxR
        while l < r:
            # if the max left height is < max right
            if maxL < maxR:
                # we'll shift our left pointer to find a higher pillar
                l += 1
                # we'll compare
                maxL = max(maxL, height[l])
                # either way, we need calculate our volume here
                # if maxL was updated and it the highest, res += 0
                # in this code part, we know the min height is left 
                res += maxL - height[l]
            else:
                # otherwise, move right ptr to try to find higher
                r -= 1
                # either moved or not, compare prev to curr position
                maxR = max(maxR, height[r])
                # if changed, then maxR-heigh[r] = 0
                # if not changed, we still know that min(maxL, maxR) = right 
                res += maxR - height[r]
        return res 


        
        
        
        
    
    
height = [0,1,0,2,1,0,1,3,2,1,2,1]     
a = Solution()
b = a.trap(height)