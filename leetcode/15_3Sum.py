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

BRUTE FORCE
    RT: O(n**3)
    Space: O(1)
HASHMAP with Fixed position
    RT: O(n**2)
    Space: O(n)
Two pointer with fixed position
    RT: O(n**2)
    Space: O(1)
Abstraction into cases


"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ''' 
        Brute Force : Three for loops 
        Runtime: O(n**3)
        Space: O(1) 
        '''
        ans = set()  
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        ans.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return list(ans) 

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        HashMap {num : idx}
        Runtime: O(n**2)
        Space: O(n)
        '''
        ans = set()
        # for each fixed NUMS[i] position
        for i in range(len(nums)):
            # create an empty hashmap and employ two sum approach
            seen = collections.defaultdict(int)
            LHS = nums[i]
            for j in range(i+1, len(nums)):
                # we know that if A+B+C=0, and we have fixed A, then each J is looking for -1(A+B)
                c = -1*(LHS + nums[j])
                # if we've prev tracked C, and it has valid occurences
                if seen[c] > 0:
                    # add
                    ans.add(tuple(sorted((LHS, nums[j], c))))
                    # then decremeent occurence
                    seen[c] -= 1
                    # and we continue the loop for the next iteration
                    continue
                # otherwise, there is no possible solution, move to next J
                seen[nums[j]] += 1
        return list(ans)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Two pointers with fixed position 
        RT: O(n**2)
        Space: O(n)
        '''
        res = set()
        nums.sort()                                         
        for i in range(len(nums)):          
            if nums[i] > 0:
                break                       
            left, right = i+1, len(nums) - 1
            while left < right:                                         
                if left >= right:
                    break
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    res.add(tuple(sorted([nums[i], nums[left], nums[right]])))
                    left += 1
                    right -= 1
        return list(res)

    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # case 1: three zeroes
        # case 2: one zero: add all cases where -num in set, and num in set
        # case 3: for negative pairs (-a,-b), find C in positive
        # case 4: for positive pairs (a, b), find -c in negative 

        # rather than looking at a data structures, algorithms perspective
        # use a general outlook approach. We have three numbers
        # in how many ways can they be arranged
        # Z + Z + Z = Z
        # P + P + N = Z
        # N + N + P = Z
        # P + N + Z = Z
        res = set()
        n, p, z = [], [], []
        for num in nums:
            if num == 0: z.append(z)
            if num > 0: p.append(num)
            if num < 0: n.append(num)
        
        N, P = set(n), set(p)

        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        if len(z) >= 3:
            res.add((0,0,0))

        for i in range(len(n)):
            for j in range(i+1, len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))

        for i in range(len(p)):
            for j in range(i+1, len(p)):
                target = -1*(p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))
        
        return list(res) 

    
#Input: nums = [-1,0,1,2,-1,-4]
#Output: [[-1,-1,2],[-1,0,1]]
alpha = Solution()
print(alpha.threeSum([-1,0,1,2,-1,-4]))
print(alpha.threeSum([]))
print(alpha.threeSum([0,0,0]))