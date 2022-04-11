# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:25:19 2022

@author: jhd9252

LeetCode Problem: 15. 3Sum
Test Cases: 318/318 tests cases passed
Runtime:  681 ms ( faster than 94.71% of Python3 submissions)
Memory Usage: 19.4 MB (less than 5.51% of Python3 online submissions for 3Sum)


Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Constraints:
   0 <= nums.length <= 3000
   -105 <= nums[i] <= 105
"""

# given an array of integers
# return all the triples [i,j,k] such that the sum [i,j,k] = 0
# i != j != k # indexes cannot be the same
# solution set must not contain duplicates
class Solution:
    def threeSum(self, nums):
        """
        
        # 315/318 test cases passed
        # time limit exceeded on test case 316
        # edge case that len(nums) < 3
        res = []
        if len(nums) < 3:
            return res
        # edge case that only zeroes. Where len(nums) >=3
        z = True
        for num in nums:
            if num != 0:
                z = False
                break
        if z:
            return [[0,0,0]]
        nums = sorted(nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                target = 0 - nums[i] - nums[j]
                if target in nums:
                    k = nums.index(target)
                    if (i!=j) and (i!=k) and (k!=j):
                        if sorted([nums[i],nums[j],nums[k]]) not in res:
                            res.append(sorted([nums[i],nums[j],nums[k]]))
        return res
        """
        # create var = set() to cross ref solutions when we add them
        res = set()
        # edge case 1: where len(nums) <3 -> return res = []
        if len(nums) < 3:
            return res
        # set up rest of cases
        # partition set into negative integers, zeroes, positive integers for faster look up times
        n, z, p = [], [], []
        for num in nums:
            if num > 0: p.append(num)
            elif num < 0: n.append(num) 
            else: z.append(num)
        N, P = set(n), set(p)
        # edge case 2: add (0,0,0) if len(z) >= 3
        if len(z) >= 3:
            res.add((0,0,0))
        # edge case 3: if there is at least 1 zero, check if there is a corresponding integer in negatives and positives 
        # such that sum == 0
        if len(z) >= 1:
            for i in N:
                if -1*i in P:
                    res.add(tuple(sorted([i, 0, -1*i])))
        # edge case 4: check all pairs of negative integers, corresponding positive integer
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))
        # edge case 5: check all pairs of positive integers, corresponding negative integer
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))
        # at this point, our res set() contains all possible (0,0,0), (n, p, p) and (n,n,p) solutions
        # convert all tuples into lists, convert res to list, return
        return list(map(list, res))
            
    
#Input: nums = [-1,0,1,2,-1,-4]
#Output: [[-1,-1,2],[-1,0,1]]
alpha = Solution()
print(alpha.threeSum([-1,0,1,2,-1,-4]))
print(alpha.threeSum([]))
print(alpha.threeSum([0,0,0]))